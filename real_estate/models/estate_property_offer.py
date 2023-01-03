# -*- coding: utf-8 -*-
from odoo import api,fields,models
from odoo.tools.date_utils import add

class estatePropertyoffer(models.Model):
     _name = "estate.property.offer"
     _description = "This is regarding the real_estate"

     price = fields.Float(string='Price')
     status = fields.Selection(selection=[('accepted','Accepted'),('refused','Refused')])
     partner_id = fields.Many2one('res.partner',required=True )
     property_id = fields.Many2one('real.estate',string ='Property Id',required=True)
     validity = fields.Integer(string='Validity(days)',default='7')
     date_deadline=fields.Date(string='Deadline',compute="_date_deadline",inverse="_inverse_date_deadline")
     create_date = fields.Date(defaut=fields.Datetime.now(),string='Create Date')
     
     
     @api.depends("validity")
     def _date_deadline(self):
          for record in self:
               record.date_deadline= add(fields.Datetime.now(),days=record.validity)
               
      
     def _inverse_date_deadline(self):
        for record in self:
             day=record.date_deadline - record.create_date
             record.validity = day.days
     
     
     