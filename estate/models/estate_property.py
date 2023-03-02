# -*- coding: utf-8 -*-
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"
    _order = "id desc"
    _inherit = ['prototype.prototype', 'mail.thread', 'mail.activity.mixin']

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)', 'The expected price must be strictly positive.'),
        ('check_selling_price', 'CHECK(selling_price > 0)', 'The selling price must be strictly positive.')
    ]

    name = fields.Char(required=True)
    property_seq = fields.Char(string='Property Reference', required=True, readonly=True, default=lambda self:('New'))
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string='Availability Date', default=lambda self: fields.Date.today()+relativedelta(months=+3), copy=False)
    expected_price = fields.Float(string='Expected Price',required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area(sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute='_compute_garden', string='Garden Area', readonly=False, store=True)
    garden_orientation = fields.Selection(
        selection = [('north', 'North'), ('east', 'East'),
                   ('south', 'South'), ('west', 'West')], compute='_compute_garden', readonly=False, store=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection = [('new','New'),
                     ('offer_received','Offer Received'),
                     ('offer_accepted','Offer Accepted'),
                     ('sold','Sold'),
                     ('canceled','Canceled')], default='new', tracking=True, copy=False)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    user_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False, readonly=True)
    tag_ids = fields.Many2many('estate.property.tag', relation='estate_property_tag_rel', string='Property Tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offer')
    total_area = fields.Integer(compute='_compute_total_area', string='Total Area')
    best_price = fields.Float(compute='_compute_best_price', string='Best Offer')
    status = fields.Char()
    is_favorite = fields.Boolean()
    kanban_state = fields.Selection(
        [('normal', 'grey'),
        ('done', 'green'),
        ('blocked','red')], string='Kanban State')

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                if record.state =="new":
                    record.state="offer_received"
            elif record.state=="canceled":
                record.state = "canceled"
            elif record.state=="sold":
                record.state = "sold"
            elif record.state=="offer_accepted":
                record.state = "offer_accepted"
            else:
                record.state = "new"
            record.best_price = max(record.mapped("offer_ids.price"),default=0)

    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if(self.garden):
                self.garden_area = 10
                self.garden_orientation = 'east'
            else:
                self.garden_area = None
                self.garden_orientation = None

    def action_sold(self):
        for record in self:
            if(record.status != "Canceled"):
                record.status = "Accepted"
                record.state = "sold"
            else:
                raise UserError("Canceled property can't be sold")
        return True
    
    def action_cancel(self):
        for record in self:
            if(record.status != "Accepted"):
                record.status = "Canceled"
                record.state = "canceled"
            else:
                raise UserError("Sold property can't be canceled")
        return True

    @api.constrains('expected_price','selling_price')
    def _validate_expected_price(self):
        for record in self:
            if float_compare(self.expected_price*0.9, record.selling_price, precision_digits=2) == 1 and self.offer_ids:
                raise ValidationError("The selling price must be 90% or greater of expected price")

    @api.ondelete(at_uninstall=False)
    def _unlink_except_available(self):
        for record in self:
            if record.state not in ['new','canceled']:
                raise UserError("You can't delete 'offer received', 'offer accepted' or 'sold' property")

    @api.model
    def create(self, vals):
        vals['property_seq'] = self.env['ir.sequence'].next_by_code('estate.property')
        return super(EstateProperty,self).create(vals)

