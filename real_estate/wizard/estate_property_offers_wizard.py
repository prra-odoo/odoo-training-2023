# -*- coding: utf-8 -*-

from odoo import models, fields, api, Command
from dateutil.relativedelta import relativedelta

class EstatePropertyOffersWizard(models.TransientModel):
    _name = "estate.property.offers.wizard"
    _description = "On clicking wizard button, Offer will be add in all the selected properties." 
    
    price = fields.Float(string="Price")
    partner_id = fields.Many2one("res.partner", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("validity", "date_deadline", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Datetime.now() + relativedelta(days=record.validity)
                
    @api.depends("date_deadline", "create_date")    
    def _inverse_date_deadline(self):
        for record in self:
            # print(record.date_deadline)
            # print(record.create_date)
            record.validity = (record.date_deadline - record.create_date.date()).days

    # Wizard Button Method
    
    def estate_property_add_offer_btn(self):
        active_ids = self._context.get('active_ids')
        # print('------------------------------')
        # print(active_ids)
        
        for property_id in active_ids:
            property = self.env['estate.property'].browse(property_id)
            # print(property.mapped('name'))
            
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