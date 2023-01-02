# -*- coding: utf-8 -*-
from odoo import fields,models

class estatePropertyoffer(models.Model):
     _name = "estate.property.offer"
     _description = "This is regarding the real_estate"

     price = fields.Float(string='Price')
     status = fields.Selection(selection=[('accepted','Accepted'),('refused','Refused')])
     partner_id = fields.Many2one('res.partner',required=True )
     property_id = fields.Many2one('real.estate',string ='Property Id',required=True)
     