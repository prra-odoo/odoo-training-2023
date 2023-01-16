from odoo import models, fields

class EstateType(models.Model):
    _name = "estate.property.type"
    _description = "This model will describe about type of houses"

    # ordering the list view by name 
    _order = "name"

    # creating a name field that will be stored in db
    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many('estate.property', "property_type_id")



    # defining sql constraints so that user cannot set same name again
    _sql_constraints = [
        (
            'check_unique_type_name',
            'unique (name)',
            'Name of the property type should be unique!'
        )
    ]