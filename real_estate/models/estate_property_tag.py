from odoo import fields,models

class Estate_property_tag(models.Model):
        _name= "estate.property.tag"
        _description= "Estate property tag"


        name=fields.Char(required=True)

        _sql_constraints = [
        ('unique_tag_name','unique(name)','Tag name must be unique'),
    ]
    