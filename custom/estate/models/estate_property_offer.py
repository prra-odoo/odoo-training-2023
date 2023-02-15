import datetime
import dateutil.parser
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Different offers"

    price=fields.Float()
    status=fields.Selection(copy=False,
                            selection=[("accepted","Accepted"),("refused","Refused")])
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("estate.property")

    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_date",inverse="_inverse_date",readonly=False)

    @api.depends("validity")
    def _compute_date(self):
        for record in self:            
            record.date_deadline=fields.Date.today()+relativedelta(days=record.validity)

         # for record in self:            
        #     record.date_deadline=fields.Date.add(record.create_date,days=record.validity)

            
    @api.depends('date_deadline')
    def _inverse_date(self):
        for record in self:
            if record.date_deadline > fields.Date.today():
                  record.validity = (record.date_deadline - fields.Date.today()).days
            else:
                record.validity=0

    def accept_action(self):
        self.status="accepted"

    def refuse_action(self):
         self.status="refused"