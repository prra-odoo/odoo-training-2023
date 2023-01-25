# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
class estate_property_offer(models.Model):
    _name="estate.property.offer"
    _description="Offers for a property"
    _order="price desc"

    price=fields.Float()
    status=fields.Selection(
        string="Status of the offer",
        selection=[("accepted","Accepted"),("refuse","Refused")],
        copy=False
    )
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("real.estate.properties",required=True)
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")
    property_type_id=fields.Many2one("estate.property.type",related="property_id.property_type_id",store=True)

    @api.depends("validity")
    def _compute_date_deadline(self):   
        for record in self:
            if record.create_date:
                record.date_deadline=record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline=fields.Datetime.now() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            diff = record.date_deadline-record.create_date.date()
            record.validity=int(diff.days)
    
    def reject_action(self):
        for record in self:
            record.status="refuse"

    def accept_action(self):
        for record in self:
            # record.property_id.offer_ids.status='refuse'
            record.status="accepted"
            record.property_id.state="offer_accepted"
            record.property_id.selling_price=record.price
            record.property_id.buyer=record.partner_id

    _sql_constraints=[
        ('check_price','CHECK(price > 0 )','Price Must be positve ')
    ]

    @api.model
    def create(self,vals):
        a=self.env["real.estate.properties"].browse(vals['property_id'])
        a.state='offer_recieved'

        max_offer=max(a.mapped('offer_ids.price'),default=0)
        if max_offer >= vals['price']:
            raise ValidationError("Offer should be greater then best offer")
        return super().create(vals)
    
    
    