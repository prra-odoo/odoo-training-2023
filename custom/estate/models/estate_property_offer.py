from odoo import models,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta

class EstatePropertyType(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    price=fields.Float()
    status=fields.Selection(string="select the status",
    selection=[("accepted","Accepted"),("refused","Refused")],
    help="select the status")
    property_id=fields.Many2one("estate.real.property")
    partner_id=fields.Many2one("res.partner")
    
    
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute='_compute_date',inverse='_compute_inverse_date')
    @api.depends('create_date','validity')
    def _compute_date(self):
        for record in self:
            record.date_deadline=date.today()+relativedelta(days=record.validity)

    def _compute_inverse_date(self):
        for record in self:
            record.validity=(record.date_deadline-date.today()).days
