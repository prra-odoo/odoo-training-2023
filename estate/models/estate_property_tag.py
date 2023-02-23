# -*- coding: utf-8 -*-
from odoo import fields, models,api,exceptions

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description = "Estate Property Tag Model _description"
    _sql_constraints = [
        ('unique_name','UNIQUE(name)','Tag Name must be unique')
    ]
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()

    @api.constrains("name")
    def _constrain_name_unique(self):
        for record in self:
            names = [name.lower() for name in self.mapped("name")]
            if(record.name.lower() in names):
                raise exceptions.ValidationError("This name already exists")