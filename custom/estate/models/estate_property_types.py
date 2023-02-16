from odoo import fields, models

class EstatePropertyTypes(models.Model):
    _name = "estate.property.types"
    _description = "estate property types"
   
    name = fields.Char(required=True, string="Types")

    _sql_constraints = [
        ('name_types',"UNIQUE(name)",'Property Types Must be Unique')
    ]