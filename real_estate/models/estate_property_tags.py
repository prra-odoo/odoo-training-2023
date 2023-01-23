# -*- coding: utf-8 -*-
from odoo import models,fields

class estate_property_tags(models.Model):
    _name = 'estate.property.tags'
    _description = "Estate Property Tags"
    _order = "name"

    name = fields.Char("Name",required=True)
    color = fields.Integer('color')
    property_tag_ids = fields.Many2many('estate.property',string='property tags')


    _sql_constraints=[('unique_name','unique(name)','Error! Enter unique name of tag')]
