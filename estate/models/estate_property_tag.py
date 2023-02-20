from odoo import api,fields, models,exceptions

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"
    _order = "name"
    _sql_constraints = [
    ('check_tag_name_uniq', 'UNIQUE (name)', 'You can not have two property tags with the same name !')
    ]

    name = fields.Char(required=True)
    color = fields.Integer()

    @api.constrains('name')
    def _check_tag_unique_name(self):
        tag_ids = self.search([]) - self
        value = [x.name.lower() for x in tag_ids]
        if self.name and self.name.lower() in value:
            raise exceptions.ValidationError(('This tag combination already exists.'))
        return True
    