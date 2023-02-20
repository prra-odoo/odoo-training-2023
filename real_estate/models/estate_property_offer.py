from odoo import api,models,fields
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class EstateOfferProperty(models.Model):
    _name="real.estate.property.offer"
    _description="Property Offer Model"
    _order ="price desc"

    # name=fields.Char(string="name",required=True)
    price=fields.Float(string="Price")
    status=fields.Selection(string="status", selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id=fields.Many2one('res.partner',required=True)
    property_id=fields.Many2one('real.estate.properties',required=True)
    validity=fields.Integer(string="Validity", default=7)
    date_deadline=fields.Datetime(compute='_compute_date_deadline',inverse= "_inverse_date_deadline")
    property_type_id=fields.Many2one(related='property_id.type_id' , store=True)

    _sql_constraints=[
        ('price_constraints', 'CHECK(price>=0)', "Price must be Postive")
    ]

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline=record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline=fields.Datetime.now()+ relativedelta(days=record.validity)
    def _inverse_date_deadline(self):
        for record in self:
            record.validity=(record.date_deadline-record.create_date).days

    def action_accepted(self):
        for record in self:
            record.status='accepted'
            record.property_id.selling_price=record.price
            record.property_id.buyer_id=record.partner_id
            record.property_id.state='offer accepted'  
              
    def action_refused(self):
        for record in self:
            self.status='refused'

    @api.model
    def create(self,vals):
        property_id=self.env['real.estate.properties'].browse(vals['property_id'])
        property_id.state='offer recevied'
        max_offer=max(property_id.mapped('offer_ids.price'),default=0)
        if max_offer>=vals['price']:
            raise ValidationError("Offer should be greater than Best offer")
        return super().create(vals)
        

    