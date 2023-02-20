from odoo import fields, models

class EstatePropertyTypes(models.Model):
    _name = "estate.property.types"
    _description = "estate property types"
   
    name = fields.Char(required=True, string="Types")
    property_ids = fields.One2many("estate.property","property_type_id")
    _order = "name"
    sequence = fields.Integer("Sequence", default = 1)


    _sql_constraints = [
        ('name_types',"UNIQUE(name)",'Property Types Must be Unique')
    ]
