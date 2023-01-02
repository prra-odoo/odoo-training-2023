# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate advertisement module"

    name = fields.Char('Name',required=True)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type') #inverse in property type
    description = fields.Text('Details',copy=False)
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date availability',default=lambda self:fields.Datetime.now(),readonly=True)
    expected_price = fields.Float('Expected price',required=True)
    selling_price = fields.Float('Selling price',readonly=True)
    bedrooms = fields.Integer('Bedroom',default='2')
    living_area = fields.Integer('Living area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden area(sqm)')
    tag_ids = fields.Many2many("estate.property.tag", string="Tags") # orm object
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'),('offer_accepted', 'Offer Accepted'),('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new',
    )
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    total_area = fields.Float('Total Area(sqm)',compute='_compute_area')

    # offernew_ids = self.env['estate.property.offer'].search([])
    # offer_names = offernew_ids.mapped('name')

    # method to calculate total area
    @api.depends('living_area', 'garden_area')
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

#  writeoff_amount = sum(writeoff_lines.mapped('amount_currency'))