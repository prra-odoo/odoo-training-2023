# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields

class estate_Property(models.Model):
    _name="estate.properties"
    _description="Real estate properties"

    name=fields.Char('Property name',required=True)
    description=fields.Text('Property description')
    postcode=fields.Char('Postcode',required=True)
    date_availability=fields.Date('Date availability', copy=False)
    expected_price=fields.Float('expected price',required=True)
    selling_price=fields.Float('selling price',required=True, copy=False)
    bedrooms=fields.Integer('bedrooms', default=2)
    living_area=fields.Integer('living area')
    facades=fields.Integer('facades')
    garage=fields.Boolean('garage')
    garden=fields.Boolean('garden')
    garden_area=fields.Integer('garden area')
    garden_orientation = fields.Selection(string="Garden Orientation", selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active= fields.Boolean('active')
    state=fields.Selection(string="State",selection=[('new','New'),('offer_received','Offer received'),('offer_accepted','Offer accepted'),('sold','Sold',),('canceled','Canceled')],default='new',required=True)


