from odoo import models,fields

class estatePropertyType(models.Model):
    _name="estate.property.type"
    _description="estate property type"
    _order = "sequence,name"

    name= fields.Char("Type" ,required=True)
    property_ids = fields.One2many('estate.property','property_type_id', string = "All property")
    sequence = fields.Integer('Sequence', default =1)


    _sql_constraints = [
        (
            'check_property_uniqueness' , 'unique(name)',
            "Property name already exist in the database"

        )
    ]
