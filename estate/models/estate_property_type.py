from odoo import models,fields,api
from odoo.exceptions import ValidationError

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "Estate Property Type"
    _order = "name"

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")

    @api.constrains('name')
    def _check_unique_name(self):
        type_ids = self.search([]) - self
        value = [x.name.lower() for x in type_ids]
        if self.name and self.name.lower() in value:
            raise ValidationError(('The property type already Exists'))
        return True

    
    

    

