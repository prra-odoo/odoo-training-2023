from odoo import api,fields, models
from datetime import date
import dateutil.parser
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"

    price = fields.Float(string="Price")
    status = fields.Selection(copy=False,selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id = fields.Many2one("res.partner",required=True)
    property_id = fields.Many2one("estate.property",required=True)
    acceptrefusebutton = fields.Selection(selection=[('refused',"Refused"),('accepted',"Accepted")])
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date",inverse="_inverse_date")
  
    @api.depends("validity","date_deadline")
    def _compute_date(self):
        for record in self:
            record.date_deadline = fields.Date.today()+relativedelta(days=record.validity)
           
    
    @api.depends("date_deadline")
    def _inverse_date(self):
        for record in self:
            record.validity = (record.date_deadline - fields.Date.today()).days

    # def action_accepted(self):
    #     for record in self:
    #         if record.status == '':
    #             record.status = 'accepted'
    #         # else:
    #         #     record.status = 0
    #     return True