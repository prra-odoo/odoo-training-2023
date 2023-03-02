from odoo import models,fields,api
from odoo.exceptions import ValidationError

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "Estate Property Type"
    _order = "name"

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_offers")

    # for counting the amount of offers received
    @api.depends("offer_ids")
    def _compute_offers(self):
        for record in self:
            if record.offer_ids:
                record.offer_count = len(record.offer_ids)
            else:
                record.offer_count = 0

    @api.constrains('name')
    def _check_unique_name(self):
        type_ids = self.search([]) - self
        value = [x.name.lower() for x in type_ids]
        if self.name and self.name.lower() in value:
            raise ValidationError(('The property type already Exists'))
        return True

    
    

    

