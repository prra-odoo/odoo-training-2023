from odoo import models,fields,api

class Offers2Property(models.TransientModel):
    _name="real.estate.offers2property"
    _description="add an offer to many properties"
    amount=fields.Integer(default=1)
    partner_id=fields.Many2one("res.partner")
    property_ids=fields.Many2many("real.estate.property")
    def action_add_offer2properties(self):
        for record in self:
            for property in record.property_ids:
                self.env['real.estate.property.offer'].create({
                    'property_id':property.id,
                    'partner_id':record.partner_id.id,
                    'price':record.amount,        
                })
    @api.model
    def default_get(self,field):
        return super().default_get(field)
    