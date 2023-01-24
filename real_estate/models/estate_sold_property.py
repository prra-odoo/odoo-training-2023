# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateSoldProperty(models.Model):
    _name = "estate.sold.property"
    _description = "Real estate module properties"
    
    name = fields.Char(string="Title", readonly=True)
    postcode = fields.Char(string="Postcode")
    selling_price = fields.Float(string="Selling Price")
    # property_type_id = fields.Many2one('estate.property.type', string='Type')
    total_area = fields.Integer(string="Total Area (sqm)")
    # buyer_id = fields.Many2one('res.partner')
    # salesperson_id = fields.Many2one('res.users', string='Salesperson')
    