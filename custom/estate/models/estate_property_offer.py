from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Different offers"
    _rec_name="price"
    _order="price desc"

    price=fields.Float(required=True)
    status=fields.Selection(copy=False,
                            selection=[("accepted","Accepted"),("refused","Refused")],readonly=True)
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("estate.property")
    property_type_id=fields.Many2one(related="property_id.property_type_id",store=True)
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_date",inverse="_inverse_date",readonly=False)
    _sql_constraints=[
        ( "check_price","CHECK(price>0)","Price must be positive" )
    ]

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
                
        for record in self.property_id.offer_ids:
            record.status="refused"        
            record.property_id.selling_price=self.price
            record.property_id.buyer_id=self.partner_id
        self.status="accepted"
        self.property_id.state='offer accepted'

    def refuse_action(self):
        for record in self:            
            # if record.status=="accepted":
            # record.property_id.selling_price=0
            # record.property_id.buyer_id=""
            record.status="refused"