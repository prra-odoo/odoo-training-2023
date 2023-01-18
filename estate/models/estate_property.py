# -*- coding: utf-8 -*-
from odoo import models,fields

class Estate_Property(models.Model):
    _name = "estate.property"
    _description = "Property Model"

    name = fields.Char(string = 'name',required=True)
    property_type_id = fields.Many2one("estate.property.type", string = 'Property Type',)
    user_id = fields.Many2one('res.users', string='Salesperson',default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner',string = 'Buyer',copy=False)
    description = fields.Text(string = 'description')
    postcode = fields.Char(string = 'postcode', required = True)
    data_avabilability = fields.Date('Datetime')
    expected_price = fields.Float(string = 'expected price',required = True)
    selling_price = fields.Float(string = 'selling price')
    bedrooms = fields.Integer(string = 'bedrooms')
    living_area = fields.Integer(string = 'living area')
    facades = fields.Integer(string = 'facades')
    garage = fields.Boolean(string = 'garage')
    garden_area = fields.Integer(string = 'garden area')
    garden_orientation = fields.Selection(
        string = 'garden orientation',
        selection = [('north','North'),('south','South'),('east','East'),('west','West')]
    )
    state = fields.Selection(
        string = 'State',
        selection = [('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')]
    )
    tag_ids = fields.Many2many("estate.property.tag","estate_property_rel","property_id","property_tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer",'property_id',string="Offer")
    
