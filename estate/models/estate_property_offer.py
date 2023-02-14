from odoo import models,fields,api

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Real Estate Property Offers"

    price=fields.Float()
    status=fields.Selection(
        copy=False,
        selection=[('accepted','Accepted'),('refused','Refused')]
    )
    partner_id=fields.Many2one("res.partner",string="Partner", required=True)
    property_id=fields.Many2one("estate.property",string="Property Id", required=True)
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_deadline",inverse = "_inverse_deadline")
    
    @api.depends("create_date","validity")
    
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + record.validity
    
    def _inverse_deadline(self):
        for record in self:
            record.validity = record.date_deadline-record.create_date
            
    