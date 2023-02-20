from odoo import models,fields,exceptions,api

class EstatePropertyTag(models.Model):
    
    _name = "estate.property.tag"
    _description = "Property Tag Model"
    _order = 'name asc'

    name = fields.Char(required=True)
    color = fields.Integer()
    _sql_constraints = [
('name_uniq', 'unique (name)', "Property tag already exists !"),
]
    @api.constrains('name')
    def _check_unique_name(self):
        tag_ids = self.search([]) - self
        value = [x.name.lower() for x in tag_ids]
        if self.name and self.name.lower() in value:
            raise exceptions.ValidationError(('The combination is already Exist'))
        return True