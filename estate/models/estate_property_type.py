from odoo import api,fields, models,exceptions

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _sql_constraints = [
    ('check_type_name_uniq', 'UNIQUE (name)', 'You can not have two property types with the same name !')
    ]
    name = fields.Char(required=True)

    @api.constrains('name')
    def _check_type_unique_name(self):
        type_ids = self.search([]) - self
        value = [x.name.lower() for x in type_ids]
        if self.name and self.name.lower() in value:
            raise exceptions.ValidationError(('This type combination already exists.'))
        return True
    