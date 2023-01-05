# -*- coding: utf-8 -*-

from odoo import models, fields

class estatepropertytags(models.Model):
    _name = "estate.property.tags"
    _description="Property tags module"
    _order = "name desc"

    name = fields.Char(string="Name",required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('check_tag', 'unique (name)', "Tag name cannot be repeated!"),
   ]    