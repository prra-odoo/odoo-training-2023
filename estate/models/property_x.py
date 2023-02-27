from odoo import fields,models,api

class PropertyX(models.Model):
    # _name="estate.property.x"
    _description="Property that will be inherited"
    _rec_name="parentName"

    parentName=fields.Char()
    age = fields.Integer()