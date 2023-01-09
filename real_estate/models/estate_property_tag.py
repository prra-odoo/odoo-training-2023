from odoo import fields,models

class Estate_property_tag(models.Model):
        _name= "estate.property.tag"
        _description= "Estate property tag"


        name=fields.Char(required=True)