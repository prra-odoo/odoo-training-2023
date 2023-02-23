
from odoo import api,models,fields  
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero
class EstateProperty(models.Model):
    _name="estate.property"
    _description="estate property project"
    _order="id desc"

    name=fields.Char(required=True) 
    active=fields.Boolean(default=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(default=lambda self:fields.Date.today()+relativedelta(months=3),copy=False)
    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False,default=0)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer(default=0,compute="_compute_garden_area",readonly=False)
    garden_orientation=fields.Selection(
        string='Type',
        selection=[('N','North'),('S','South'),('E','East'),('W','West')],
        help="Choose direction",compute="_compute_garden_orientaion"
    )       
    state=fields.Selection(
        string='State',
        selection=[('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        default='new',
        required=True
    )
    property_type_id=fields.Many2one("estate.property.types",string="Property Type")
    buyer=fields.Many2one("res.partner",copy=False)
    salesperson=fields.Many2one('res.users',default=lambda self: self.env.user)
    tag_ids=fields.Many2many('estate.property.tag')
    offer_ids=fields.One2many('estate.property.offer','property_id')
    total_area=fields.Integer(compute="_compute_area",store=True)
    best_offer=fields.Float(compute="_compute_bestoffer",readonly=True)

    _sql_constraints=[
                (
        "check_expected_price","CHECK(expected_price>0)","Price must be positive"
                ),
        
                (
        "check_selling_price","CHECK(selling_price>-1)","Price should not be negative"
                )
                      ]
 
    @api.depends("living_area","garden_area")
    def _compute_area(self):
        for record in self:
            record.total_area=record.living_area+record.garden_area

    @api.depends("offer_ids.price")
    def _compute_bestoffer(self):
        for record in self:
            if record.offer_ids:
                if record.state=="new":
                    record.state="offer received"
                record.best_offer=max(record.offer_ids.mapped('price'))

            else:
                record.best_offer=0
                record.state="new"


    # @api.onchange("garden")
    # def _onchange_garden(self):
    #     if self.garden:
    #         self.garden_area=10
    #         self.garden_orientation='N'
    #     else:
    #         self.garden_area=0
    #         self.garden_orientation=''

    @api.depends("garden")
    def _compute_garden_orientaion(self):
        for record in self:
            if record.garden:
                record.garden_orientation='N'
            else:
                record.garden_orientation=''
    @api.depends("garden")
    def _compute_garden_area(self):
        for record in self:
            if record.garden:
                record.garden_area=10
            else:
                record.garden_area=0

    @api.constrains("selling_price")
    def _check_offer_price(self):
        for record in self:
            sp=(90*record.expected_price)/100
            if((not float_is_zero(record.selling_price,precision_rounding=0.01)) and 
                float_compare(sp,record.selling_price,precision_rounding=0.01)>=0):
                raise ValidationError("The selling price must be at least 90% of the expected price! You must reduce the expected price if want to accept this offer")
                
                        
      


    def sold_action(self):
        for record in self:
            if record.selling_price==0:
                if record.state=='canceled' :
                    raise UserError("Canceled Propery cannot be sold")
            else:
                record.state='sold'

    def cancel_action(self):
        for record in self:
            if record.selling_price==0:
                if record.state=='sold':
                    raise UserError("Sold Propery cannot be canceled")
            else:
                record.state='canceled'
        