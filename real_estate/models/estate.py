from odoo import api, models, fields
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class Estate(models.Model):
    _name="real.estate.properties"
    _description="Property Model"
    _order ="id desc"

    name=fields.Char(string="Title",required=True)
    description=fields.Text('Description')
    postcode=fields.Char('Postcode')
    date_availability=fields.Date('Date Availabilty',copy=False,default=date.today()+relativedelta(months=3))
    expected_price=fields.Float('Expected Price',required=True)
    selling_price=fields.Float('Selling Price',copy=False)
    bedrooms=fields.Integer('Bedrooms',default=2)
    living_area=fields.Integer('Living Area')
    facades=fields.Integer('Facades')
    garage=fields.Boolean('Garage')
    garden=fields.Boolean()
    garden_area=fields.Integer(compute='_compute_garden',store=True,readonly=False)
    garden_orientation=fields.Selection(selection=[('north','North'), ('south','South'), ('east','East'),('west','West')])
    active=fields.Boolean(default=True)
    state=fields.Selection(selection=[('new','New'),('offer recevied','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],default='new' ,copy=False)
    type_id=fields.Many2one('real.estate.property.type',string="Property type")
    user_id = fields.Many2one('res.users', string='Salesperson',default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    tag_ids = fields.Many2many('real.estate.property.tag',string="Property Tags")
    offer_ids = fields.One2many('real.estate.property.offer','property_id',string="Property Offer")
    total_area=fields.Float(compute='_compute_total_area')
    best_offer=fields.Integer(compute='_compute_best_offer')
    _sql_constraints = [
        ('expected_price_constraints', 'CHECK(expected_price>=0)', "A Expected Price must be postive."),
        ('selling_price_constraint','CHECK(selling_price>=0)',"A Selling Proce Must be postive"),
    ]
   




    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            print(record.offer_ids.mapped('price'))
            record.best_offer = max(record.offer_ids.mapped('price'),default=0)
            # ids = [l.price for l in record.offer_ids]
            # print(ids)
            # record.best_offer = max(ids)


    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if record.garden:
                record.garden_area=10
                record.garden_orientation='north'
            else:
                record.garden_area=0
                record.garden_orientation=''

    def action_sold(self):
        for record in self:
            if record.state=="canceled":
                raise UserError("A canceled property cannot be sold")
            record.state="sold"

    def action_canceled(self):
        for record in self:
            if record.state=="sold":
                raise UserError("A sold property cannot be Canceled")
            record.state="canceled"

    @api.constrains('selling_price')
    def check_selling_price(self):
        for record in self:
            # if record.selling_price<=0.90 * record.expected_price:
            #     raise ValidationError("Selling Price Must be 90% of Expected Price")
            for record in self:
                if (not float_is_zero(record.selling_price, precision_rounding=0.1)) and float_compare(record.selling_price, 0.9* record.expected_price,precision_rounding=0.1) == -1:
                    raise ValidationError("selling price cannot be less than 90% of expected price")
