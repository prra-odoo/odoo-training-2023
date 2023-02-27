from odoo import api,fields, models,exceptions

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _order = "sequence,name"
    _sql_constraints = [
    ('check_type_name_uniq', 'UNIQUE (name)', 'You can not have two property types with the same name !')
    ]
    
    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property","property_type_id")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    @api.constrains('name')
    def _check_type_unique_name(self):
        type_ids = self.search([]) - self
        value = [x.name.lower() for x in type_ids]
        if self.name and self.name.lower() in value:
            raise exceptions.ValidationError(('This type combination already exists.'))
        return True

    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer(compute="_compute_offer_count")
    
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
    
    