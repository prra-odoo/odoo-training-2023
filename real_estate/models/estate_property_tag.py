from odoo import fields,models

class Estate_property_tag(models.Model):
        _name= "estate.property.tag"
        _description= "Estate property tag"
        _order = "name"


        name=fields.Char(required=True)
        color = fields.Integer()

        _sql_constraints = [
        ('unique_tag_name','unique(name)','Tag name must be unique'),
    ]
    