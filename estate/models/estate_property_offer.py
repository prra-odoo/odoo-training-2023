from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description = "Estate Property Type"

    price = fields.Float()
    status = fields.Selection(string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="What's the Status!",default="new", copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(default=7)

    create_date = fields.Date(default=fields.date.today())

    date_deadline = fields.Date(compute="compute_date_deadline", inverse="inverse_date_deadline", string="Deadline")
    @api.depends('create_date','validity')
    def compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=record.validity)  
    def inverse_date_deadline(self):
        for record in self:
            record.validity =  (record.date_deadline - record.create_date).days

    # def action_accept(self):
    #     for record in self.search([('status','=','accepted')]):
    #         if record.property_id == self.property_id:
    #             raise ValidationError("Can't accept more than one")
    #         else:
    #             for i in record:
    #                 record.status='refused'
    #         self.status='accepted'
    #         self.property_id.status='offer_accepted'
    #         self.property_id.selling_price = self.price
    #         self.property_id.buyers_id = self.partner_id

    


    

    

