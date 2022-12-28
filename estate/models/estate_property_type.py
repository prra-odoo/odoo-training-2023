# -*- coding: utf-8 -*-

from odoo import models,fields

class estatePropertyType(models.Model):
    _name ="estate.property.type"
    _description="This model defines the property type for Estate Property Module"

    name = fields.Char(required=True)
    


