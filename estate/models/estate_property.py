# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate_property Model"
    _order ="id desc"
    _inherit = "prototype.prototype" 
    _inherit = ['mail.thread', 'mail.activity.mixin']

# -*- Constraints Selction -*-
    _sql_constraints = [
        ('check_expected_price',
        'CHECK(expected_price > 0)',
        'Expected Price Must be Positive'),
        ('check_selling_price',
        'CHECK(selling_price > 0)',
        'Selling Price Must be Positive'),
    ]

# -*- Field Selction -*-
    name = fields.Char(required=True)
    description = fields.Text()
    property_seq = fields.Char(string="Seq. No.", readonly=True, required=True, default=lambda self:('New'))
    postcode = fields.Char(required=True)
    date_availability = fields.Date(
        default=lambda self: fields.Date.today() + relativedelta(months=3), copy=False)
    property_image = fields.Binary()
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute='_compute_garden_fields',store=True, readonly=False)
    garden_orientation = fields.Selection(
        string='Garden Orientattion',compute='_compute_garden_fields',store=True, readonly=False,
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')],
    )
    total_area = fields.Integer(compute = "_compute_total_area")
    best_price = fields.Float(compute = "_compute_best_price")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="Status",
        selection=[('new', 'New'), ('offer_recieved', 'Offer Recieved'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        required=True,
        copy=False,
        default='new',
        tracking=True
    )
    user_id = fields.Many2one(comodel_name='res.users', string='Salesperson',
                              index=True, default=lambda self: self.env.user)
    buyer_id=fields.Many2one(comodel_name='res.partner',string='Buyer',index=True)
    property_type_id = fields.Many2one(comodel_name='estate.property.type',index=True)
    tag_ids = fields.Many2many(comodel_name='estate.property.tags',relation='tag_table',required=True)
    offer_ids=fields.One2many(comodel_name='estate.property.offers',inverse_name='property_id') 
    is_favorite = fields.Boolean()
    kanban_state = fields.Selection(
        [('normal', 'grey'),
        ('done', 'green'),
        ('blocked','red')], string='Kanban State')

# -*- Business Logic Selction -*-
    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                if record.state =="new":
                    record.state="offer_recieved"
            elif record.state=="cancelled":
                record.state = "cancelled"
            elif record.state=="sold":
                record.state = "sold"
            elif record.state=="offer_accepted":
                record.state = "offer_accepted"
            record.best_price = max(record.mapped("offer_ids.price"),default=0)

    # @api.depends('offer_ids')
    # def _compute_best_price(self):
    #     for record in self:
    #         if(record.offer_ids):
    #             record.best_price = max(offer.price for offer in record.offer_ids)
    #         else:
    #             record.best_price = 0.0

    @api.depends("garden")
    def _compute_garden_fields(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False 

    def action_sold(self):
        for record in self:
            if record.state != "cancelled":
                record.state = "sold"
            else:
                raise UserError("This property can not be sold because it was cancelled")
        return True
    
    def action_cancel(self):
        for record in self:
            if record.state != "sold":
                record.state = "cancelled"
            else:
                raise UserError("This property can not be cancelled because it was sold")
        return True
            
    # @api.constrains('expected_price')
    # def _check_expected_price(self):
    #     for record in self:
    #         if record.expected_price <= 0:
    #             raise ValidationError("Expected Price Must be Positive")

    # @api.constrains('bedrooms')
    # def _check_bedrooms(self):
    #     for record in self:
    #         if record.bedrooms < 2:
    #             raise ValidationError("Bedrooms must be more than 1")

    # _sql_constraints = [
    #     ('check_bedrooms',
    #     'CHECK(bedrooms > 1)',
    #     'Bedrooms must be more than 1')
    # ]


    @api.constrains('expected_price','selling_price')
    def _validate_expected_price(self):
        for record in self:
            if float_compare(self.expected_price*0.9, self.selling_price, precision_digits=2) == 1 and self.offer_ids:
                raise ValidationError("The selling price must be minimum 90% of the Expected Price")

    @api.ondelete(at_uninstall=False)
    def _unlink_except_available(self):
        for record in self:
            if record.state not in ['new','cancelled']:
                raise UserError("Property can only delete when state is in new or cancelled")

    @api.model
    def create(self, vals):
        vals['property_seq'] = self.env['ir.sequence'].next_by_code('estate.property')
        return super(EstateProperty, self).create(vals)