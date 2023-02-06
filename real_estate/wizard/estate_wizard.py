from odoo import fields,api,models,Command
from dateutil.relativedelta import relativedelta
from datetime import date

class Creating_propertywizard(models.TransientModel):
    _name="property.estate.offers"
    _description = "To create wizard for propeties"

    price = fields.Float()
    partner_id= fields.Many2one("res.partner")
    validity = fields.Integer(default="7")
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")


    def add_offer(self):
        active_ids = self._context.get('active_ids')
        
        for property_id in active_ids:
            property = self.env['estate.property.model'].browse(property_id)
            
            property.write({
                "offer_ids": [
                    Command.create({
                        "price": self.price,
                        "partner_id": self.partner_id.id,
                        "validity": self.validity,
                        "date_deadline": self.date_deadline,
                    })
                ],
            })

    @api.depends('validity','create_date')
    def _compute_deadline(self):

        for record in self:
            # print("-----------------", record.create_date)
            if record.create_date == True:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = date.today() + relativedelta(days=record.validity)

    def _inverse_deadline(self):
        
        for record in self:  
            record.validity=abs(record.create_date.date() - record.date_deadline).days