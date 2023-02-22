from odoo import models, fields

class EstatePropertyType(models.Model):
    _name= "estate.property.type"
    _description = "this is a estate property module "
    _order = "sequence desc"

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property","property_type_id")
    sequence = fields.Integer('Sequence',default=1)

    # Sql contrainsts
    _sql_constraints = [
        ("unique_name","UNIQUE(name)","A property type name must be unique"),
    ]