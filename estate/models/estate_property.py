# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare

class EstateModel(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    name = fields.Char('Name',required = True)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date('Date availability', readonly = True, default=lambda self: fields.datetime.now()+ relativedelta(months=3))
    expected_price = fields.Float('Expected price', required = True)
    selling_price = fields.Float('Selling price', copy = False)
    bedrooms = fields.Integer()
    living_area = fields.Integer('Living area')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer('Garden area')
    garden_orientation = fields.Selection(
            string='Garden orientation type',
            selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
        )
    active = fields.Boolean(default=True)
    state = fields.Selection(
            selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], default="new", tracking=True 
        )
    property_type_id = fields.Many2one('estate.property.type')
    buyers_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    sales_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.uid)
    tags_ids = fields.Many2many("estate.property.tags", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_max_price", default=0)
    company_id = fields.Many2one("res.company", string="Company", default=lambda self: self.env.user.company_id)

    _sql_constraints = [
        ('check_expected_selling_price', 'CHECK(expected_price >= 0 AND selling_price >=0)',
         'The price should be positive')
    ]

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_max_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'), default=0)

    def action_sold(self):
        for record in self:
            if record.state == "canceled":
                raise UserError("Canceled property cannot be sold")
            else:
                record.state = "sold"
        return True

    def action_canceled(self):
        for record in self:
            if record.state == "sold":
                raise UserError("Sold property cannot be canceled")
            else:
                record.state = "canceled"
        return True 

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if not float_is_zero(record.selling_price, precision_rounding=0.01):
                if float_compare(record.selling_price, 0.9*record.expected_price, precision_digits=2)==-1:
                    raise UserError("Selling price should be greater than 90 percentage of expected price")

    @api.ondelete(at_uninstall=False)
    def _deleting_the_record(self):
        if self.state in ['offer_received', 'offer_accepted', 'sold']:
            raise UserError("only new and canceled property can be deleted")
