from odoo import models,fields,api

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="Estate Property Tag"

    name=fields.Char(string="Property Tag",required=True)