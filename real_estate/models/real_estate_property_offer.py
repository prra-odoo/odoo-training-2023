from odoo import fields,models,api,_
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from datetime import datetime
class RealEstatePropertyOffer(models.Model):
    _name="real.estate.property.offer"
    _description="Property Offer"
    _order="price desc"
    price=fields.Float()
    status=fields.Selection(selection=[("accepted","Accepted"),("refused","Refused")],copy=False)
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("real.estate.property",required=True,ondelete="cascade")
    property_type_id=fields.Many2one(related="property_id.type_id",store=True)
    validity=fields.Integer(default=7)
    date_deadline=fields.Datetime(compute="_compute_date_deadline",inverse="_inverse_date_deadline")
    _sql_constraints=[('offer_price_constraint','CHECK(price>0)','Offered price must be strictly positive')]
    def action_status_accepted(self):
        for record in self:
            record.property_id.offers_ids.status='refused'
            record.status='accepted'
            record.property_id.state='offer_accepted'
            record.property_id.selling_price=record.price
            record.property_id.buyer_id=record.partner_id
    def action_status_refused(self):
        for record in self:
            record.status='refused'
    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline=record.create_date+relativedelta(days=record.validity)
            else:
                record.date_deadline=fields.Datetime.now()+relativedelta(days=record.validity)
    def _inverse_date_deadline(self):
        for record in self:
            diff=record.date_deadline-record.create_date
            record.validity=int(diff.days)
    @api.model
    def create(self,vals):
        property_id=self.env['real.estate.property'].browse(vals['property_id'])
        property_id.state='offer_received'
        if vals['price']<property_id.best_offer:
            raise UserError(_("New offer cannot be less than the previous offer"))
        return super().create(vals)
