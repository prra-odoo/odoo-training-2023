# -*- coding: utf-8 -*-
from odoo import models,fields
class Estate_Property_Tag(models.Model):
    _name="estate.property.tag"
    _description="Tags of Property"

    name=fields.Char(required=True)

    _sql_constraints=[
        ('unique_tags','UNIQUE(name)','The tag you are trying to create is already exist')
    ]