from odoo import models,fields,api
from odoo.exceptions import ValidationError

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description = "Estate Property Tag"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()

    @api.constrains('name')
    def _check_unique_name(self):
        tag_ids = self.search([]) - self
        value = [x.name.lower() for x in tag_ids]
        if self.name and self.name.lower() in value:
            raise ValidationError(('The tag already Exists'))
        return True
    

    

