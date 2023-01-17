# -*- coding: utf-8 -*-

from odoo import api,models,_,fields
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from odoo.tools import float_is_zero,float_compare

class estateModel(models.Model):
    _name = "estate.property"
    _description = "Real Estate Module"
    _inherit = ['mail.thread','mail.activity.mixin']
    _order = "id desc"
    
    name = fields.Char('Name',required=True)
    description = fields.Text('Description',copy=False,required=True)
    postcode = fields.Char('Post Code',required=True)
    date_availability = fields.Date('Date Avilability',default=lambda self: fields.datetime.today()+relativedelta(months=3))
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price',default=0)
    bedrooms = fields.Integer('Bedrooms',required=True)
    living_area = fields.Integer('Living Area',copy=False)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    active = fields.Boolean(default=True)
    state=fields.Selection(selection=[('new', 'New'), ('offerrecieved', 'Offer Recieved'),('offeraccepted','Offer Accepted'),('sold','Sold'),('cancel','Cancel')],
        default='new',tracking=True,required=True)
    garage_orientation = fields.Selection(
        string='Garden Orientation:',       
        selection=[('east', 'East'), ('west', 'West'),('north','North'),('south','South')])
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")
    property_type_id=fields.Many2one("estate.property.type", string="Property")
    tags_ids=fields.Many2many("estate.property.tags",string="Tags")
    offer_ids=fields.One2many("estate.property.offer","property_id",string="Property Offers",readonly=False)
    sales_id=fields.Many2one("res.users",string="Sales",default=lambda self: self.env.user)
    buyers_id=fields.Many2one("res.partner",string="Buyers")

    _sql_constraints=[
        ('check_expected_price','CHECK(expected_price >= 0)','Expected Price cannot be negative'),
        ('check_selling_price','CHECK(selling_price >= 0)','Selling cannot be negative')
    ]


    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(self.offer_ids.mapped('price'),default=0)

    def action_to_sold(self):
        for record in self:
            if record.state =='cancel':
                raise ValidationError(_("Canceld Property Cannot be Sold"))
            else:
                record.state ='sold'

    def action_to_cancel(self):
        for record in self:
            if record.state =='sold':
                raise ValidationError(_("Sold Property Cannot be Cancled"))
            else:
                record.state ='cancel'

    @api.model
    def get_empty_list(self,name):
        if not self.env.ref('name', raise_if_not_found=False):
            return '<p class="o_view_nocontent_smiling_face">%s</p>' % _('No record found, create one :)')

    @api.constrains('selling_price','expected_price')
    def _check_constrains_SP(self):
        for record in self:
            if not float_is_zero(record.selling_price,precision_rounding=0.01):
                if float_compare(record.selling_price,0.9*record.expected_price,precision_digits=2)==-1:
                    raise ValidationError("Selling Price Cannot be less than 90percent of Expected Price")


    @api.ondelete(at_uninstall=False)
    def _unlink_excep_new_cancled_user(self):
        for record in self:
            if record.state=='new' or record.state=='cancel' :
                pass    
            else:
                raise ValidationError("Error")