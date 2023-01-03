# -*- coding: utf-8 -*-

from odoo import api,models,_,fields
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class estateModel(models.Model):
    _name = "estate.property"
    _description = "Real Estate Module"
    
    name = fields.Char('Name',required=True)
    description = fields.Text('Description',copy=False,required=True)
    postcode = fields.Char('Post Code',required=True)
    date_availability = fields.Date('Last Availability',default=lambda self:fields.Datetime.today())
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price',copy=False,required=True)
    bedrooms = fields.Integer('Bedrooms',required=True)
    living_area = fields.Integer('Living Area',copy=False)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    active = fields.Boolean(default=True)
    state=fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('done','Done'),('cancel','Cancel')],default='new')
    garage_orientation = fields.Selection(
        string='Garden Orientation:',
        selection=[('east', 'East'), ('west', 'West'),('north','North'),('south','South')],
        help="Type is used to separate Leads and Opportunities")
    total_area = fields.Float(compute="_compute_total_area")
    property_id=fields.Many2one("estate.property.type", string="Property")
    tags_ids=fields.Many2many("estate.property.tags",string="Tags")
    offer_ids=fields.One2many("estate.property.offer","property_id",string="Property Offers")
    sales_id=fields.Many2one("res.users",string="Sales",default=lambda self: self.env.user)
    buyers_id=fields.Many2one("res.partner",string="Buyers")
    best_price=fields.Float(compute="_compute_bestprice",string="Best Offer")

    # sellprice=fields.Float(compute="_compute_Selling_price",string="Final Selling Price")



    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_bestprice(self):
        for record in self:
            record.best_price = max(self.offer_ids.mapped('price'),default=0)

    def action_to_sold(self):
        for record in self:
            if record.state =='cancel':
                raise ValidationError(_("Canceld Property Cannot be Sold"))
            else:
                record.state='done'

    def action_to_cancel(self):
        for record in self:
            if record.state =='done':
                raise ValidationError(_("Sold Property Cannot be Cancled"))
            else:
                record.state='cancel'

    # @api.depends('offer_ids.status')
    # def _compute_Selling_price(self):
    #     for record in self:
    #         record.sellprice = record.offer_ids.price
