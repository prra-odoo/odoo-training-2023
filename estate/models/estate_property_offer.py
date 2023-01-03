# -*- coding: utf-8 -*-

from odoo import models, fields , api
from dateutil.relativedelta import relativedelta
from odoo.tools.date_utils import add,subtract

class estateOffer(models.Model):
    _name="estate.property.offer"
    _description = "This is the estate property offer model"
    
    price = fields.Float()
    status = fields.Selection(string = "status",selection = [('accepted','Accepted'),('refused','Refused')])
    create_date = fields.Date(default = lambda self: fields.datetime.today(),readonly=True)
    validity = fields.Integer("Validity",default=7)
    date_deadline = fields.Date("Deadline" ,compute="_compute_deadline_" , inverse = "_compute_validty_changes_")
    partner_id = fields.Many2one("res.partner",string="Partner id",)
    property_id= fields.Many2one("estate.property",string="Property id")
    state = fields.Selection(string='Status',selection=[('accepted','Accepted'),('refused','Refused')])
    
    @api.depends('create_date','validity','date_deadline')
    def _compute_deadline_(self):
        for record in self:
            record.date_deadline = add(record.create_date,days=record.validity)
            # record.date_deadline = record.create_date + relativedelta( months =+ record.validity)
            
    def _compute_validty_changes_(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
            
    