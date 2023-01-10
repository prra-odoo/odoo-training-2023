# -- coding: utf-8 --

from odoo import fields, models ,api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate model"
    _order = "id desc"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char('Name :', required = True)
    description = fields.Text('Description ')
    postcode = fields.Char('Postcode ')
    date_availability = fields.Date(default=lambda self: fields.Datetime.now())
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer('Bedrooms ')
    living_area = fields.Integer('Living Area ')
    facades = fields.Integer('Facades ')
    garage = fields.Boolean('Garage ')
    garden = fields.Boolean('Garden ')
    garden_area = fields.Integer('Garden Area ')
    garden_orientation = fields.Selection(string="Orientation ",
        selection=[('north', 'North'), ('south', 'South'), ('east','East'), ('west','West')],
        help="Type is used to separate Leads and Opportunities")
    state = fields.Selection(selection= [('new','New'),('cancel','Cancel'),('offer_recieved','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold')], default="new",tracking=True)
    activate = fields.Boolean(default=True)
    property_type_id = fields.Many2one("estate.property.type",string= "Property type")
    salesman_id=fields.Many2one("res.users",string="salesman",default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyers")
    tag_ids = fields.Many2many("estate.property.tag", string= "Property tag")
    offer_ids = fields.One2many("estate.property.offer","property_id")
    total_area= fields.Float(compute='_compute_total_area')
    best_price = fields.Float(compute='_compute_best_price')
    status =fields.Char()

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
        
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'),default=0)

    def sold_action(self):
        for record in self:
            if record.status=='cancel':
                raise UserError(('Cancel Property can not be sold'))
            else:
                record.status='Sold'
                record.state='sold'

    def cancel_action(self):
        for record in self:
            if record.status=='sold':
                raise UserError(("Sold property can't be canceled"))
            else:
                record.status='Cancel'
                record.state='cancel'


    @api.constrains("expected_price", "selling_price")
    def _check_price_difference(self):
        for prop in self:
            if (
                not float_is_zero(prop.selling_price, precision_rounding=0.01)
                and float_compare(prop.selling_price, prop.expected_price * 90.0 / 100.0, precision_rounding=0.01) < 0
            ):
                raise ValidationError(
                    "The selling price must be at least 90% of the expected price! "
                    + "You must reduce the expected price if you want to accept this offer."
                )
            
    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0)", "The expected price must be positive"),
        ("check_selling_price", "CHECK(selling_price >= 0)", "The selling price must be positive"),
    ]