from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_compare,float_is_zero


class EstateModel(models.Model):
    _name="estate.property"
    _description = "Testing an Estate Module"
    _order="id desc"

    name = fields.Char(required=True,default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default= lambda self: fields.Datetime.now()+relativedelta(month=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean(compute="_compute_garden_field",readonly=False,store=True)
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('north','North'), ('south','South'), ('east','East'), ('west','West')],
        compute='_compute_garden_fields',
        help = 'Select one from Below ', 
        store=True,
        readonly=False,)
    state = fields.Selection(
        selection = [('new','New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'),
                      ('sold', 'Sold'), ('canceled', 'Canceled')  ],
                      default='new')
    active = fields.Boolean(default=True)
    # Linking Others Modules
    property_type_ID= fields.Many2one('estate.property.type',string="estate_type_partner")
    buyer_id=fields.Many2one('res.partner')
    salesperson_id = fields.Many2one('res.users', default= lambda self : self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string="estate_tags")
    offer_ids = fields.One2many('estate.property.offer',"property_id")
    total_area = fields.Integer(compute="_compute_total_area")
    best_offer= fields.Integer(compute="_compute_best_price")
    user_id = fields.Many2one('res.users')
    seq_name = fields.Char(string='Sequence', default=lambda self: ('New'))
    # estate_delig_ids = fields.One2many('estate.deligation.test','estate_delig')
    

    _sql_constraints=[(
        'selling_price_positive','CHECK(selling_price>0)',
        'Selling price Must be Positive')]

    _sql_constraints = [
        ('check_expected_price',
        'CHECK(expected_price > 0)',
        'Expected Price Must be Positive')
    ]

    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('estate.property')
        return super(EstateModel,self).create(vals)
    

    @api.ondelete(at_uninstall=False)
    def _unlink_except_available(self):
        for record in self:
            if record.state not in ['new','canceled']:
                raise UserError("!!")



    @api.constrains('selling_price','expected_price')
    def _check_selling_price(self):
        for record in self:
            sp = (90 * record.expected_price) / 100
            if(not float_is_zero(record.selling_price, precision_rounding=0.01)):
                if (float_compare(sp,record.selling_price, precision_rounding=0.01) >= 0):
                    raise ValidationError("The selling price must be at least 90% of the expected price! You must reduce the expected price if you want to accept this offer.")

    @api.depends("garden_area","living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area= record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                if record.state=="new":
                    record.state="offer received"
            elif record.state =="canceled":
                record.state="canceled"
            else:
                record.state="new"
            record.best_offer = max(record.mapped("offer_ids.price"),default=0)

    @api.depends("garden")
    def _compute_garden_fields(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0
                record.garden_orientation = None
            # SOLD BUTTON IN FORM
    def sold_action_button(self):
        for record in self:
            if record.state == "canceled":
                raise UserError('Cancelled properties cannot be sold.')
            # elif record.state == "canceled":
            #     record.state =="canceled"
            else:
                record.state='sold'
            # CANCEL BUTTON IN FORM
    def cancel_action_button(self):
        for record in self:
            if record.state == "sold":
                raise UserError("Sold property cant't be cancelled")
            else:
                record.state="canceled"
            #CLASSIC INHERITANCE
class ResUsers(models.Model):
    _inherit="res.users"

    property_ids = fields.One2many('estate.property','user_id',domain=[('state','in',['new','offer received'])])
    testing = fields.Char()



