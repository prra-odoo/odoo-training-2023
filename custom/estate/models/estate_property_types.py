from odoo import fields, models

class EstatePropertyTypes(models.Model):
    _name = "estate.property.types"
    _description = "estate property types"
   
    name = fields.Char(required=True, string="Types")