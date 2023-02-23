from odoo import fields,models,api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "It's a Estate Property Offer"
    _order = "price desc"
    _sql_constraints = [
        ("check_offer_price","CHECK(price>=0)","An offer price must be strictly positive"),
    ]
    price = fields.Float()
    status  = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused')
    ],
    copy=False,
    )
    partner_id = fields.Many2one("res.partner",string="buyer",required=True)
    property_id = fields.Many2one("estate.property",string="Property ID",required=True)
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(compute = "_compute_date_deadline",inverse="_inverse_date_deadline")

    # Computed Methods
    @api.depends("validity","create_date")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity) 
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)
        return True
    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days
    
    # Actions Methods

    def action_set_status_accepted(self):
        for record in self.property_id.offer_ids:
            record.status = "refused"   
        self.status="accepted"
        self.property_id.state = "offer_accepted"
        self.property_id.buyer_id = self.partner_id
        self.property_id.selling_price = self.price
        return True
    
    def action_set_status_refused(self):
        for record in self: 
            record.status = "refused"
        return True

    # Auto calle
