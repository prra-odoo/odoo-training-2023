from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description = "Estate Property Type"
    _sql_constraints = [
                    ('name', 'UNIQUE (name)', 'You can not have two properties with the same name !')
                ]
    _order = "price desc"
    _rec_name="price"

    price = fields.Float()
    status = fields.Selection(string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="What's the Status!", copy=False)

    partner_id = fields.Many2one("res.partner", string="Partner", required=True )
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(default=7)

    #Related Fields: You cannot chain Many2many or One2many fields in related fields dependencies. 
    #                Related can be used to refer to a One2many or Many2many field on another model on the condition 
    #                that it’s done through a Many2one relation on the current model. One2many and Many2many 
    #                are not supported and the results will not be aggregated correctly:

    property_type_id = fields.Many2one("estate.property.type",string="Property Type",related='property_id.property_type_id', store=True)

 
    #create_date = fields.Date(default=fields.date.today())

    date_deadline = fields.Date(compute="compute_date_deadline", inverse="inverse_date_deadline", string="Deadline")
    @api.depends('create_date','validity')
    def compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity) 
            else:
                record.date_deadline = fields.date.today() + relativedelta(days=record.validity)
                  
    def inverse_date_deadline(self):
        for record in self:
            if(record.date_deadline > fields.date.today()):
                record.validity =  (record.date_deadline - record.create_date.date()).days
            else:
                raise ValidationError("Enter a validation date beyond today's date!")


    def accept_offer(self):
        for offers in self.property_id.offer_ids:
            offers.status = "refused"
        self.status="accepted"
        self.property_id.state="offer accepted"
        self.property_id.selling_price=self.price
        self.property_id.buyer_id=self.partner_id
        return True

    def refuse_offer(self):
        self.status = "refused"

    color = fields.Integer(compute="_compute_color")
    @api.depends('status')
    def _compute_color(self):
        for record in self:
            if (record.status=='accepted'):
                record.color=10
            elif (record.status=='refused'):
                record.color=1
            else:
                record.color=3

    @api.model
    def create(self, vals):
        if(vals['price']<self.env['estate.property'].browse(vals['property_id']).best_offer):
            raise ValidationError("Offer Price cannot be less than best offer.")
        self.env['estate.property'].browse(vals['property_id']).state = 'offer recieved'
        return super().create(vals)
    

    
    

    


    

    

