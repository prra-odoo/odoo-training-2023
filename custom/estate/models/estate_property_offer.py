from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class EstatePropertyType(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _sql_constraints=[ ('price_check','CHECK(price>0 and price != 0)',"offer price must be strictly positive")

    ]
    price = fields.Float()
    status = fields.Selection(string="select the status",
                              selection=[("accepted", "Accepted"),
                                         ("refused", "Refused")],
                              help="select the status")
    property_id = fields.Many2one("estate.real.property")
    partner_id = fields.Many2one("res.partner")

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(
        compute='_compute_date', inverse='_compute_inverse_date')

    @api.depends('create_date', 'validity')
    def _compute_date(self):
        for record in self:
            record.date_deadline = date.today()+relativedelta(days=record.validity)

    def _compute_inverse_date(self):
        for record in self:
            if(record.date_deadline>date.today()): 
                record.validity = (record.date_deadline-date.today()).days
            else:
                record.validity=0.0
    @api.depends('property_id','price')
    def action_accept(self):
        for record in self:
                record.status='accepted'
                record.property_id.selling_price=record.price
                
                    
    def action_refused(self):
        for record in self:
            record.status='refused'
            record.property_id.selling_price=0.00