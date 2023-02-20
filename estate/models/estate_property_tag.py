from odoo import models,fields,api

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="Estate Property Tag"
    _order="name"

    name=fields.Char(string="Property Tag",required=True)
    color=fields.Integer()

    _sql_constraints=[
        ('unique_tag','unique(name)','Property Tag must be unique')
    ]