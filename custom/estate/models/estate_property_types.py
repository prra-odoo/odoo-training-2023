from odoo import api,fields, models

class EstatePropertyTypes(models.Model):
    _name = "estate.property.types"
    _description = "estate property types"
   
    name = fields.Char(required=True, string="Types")
    property_ids = fields.One2many("estate.property","property_type_id")
    _order = "name"
    sequence = fields.Integer("Sequence", default = 1)
    offer_ids=fields.One2many("estate.property.offer","property_type_id")
    offer_count=fields.Integer(compute = "_compute_offer_count")

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            if record.offer_ids:
                record.offer_count=len(record.offer_ids)
            else:
                record.offer_count=0
            
    _sql_constraints = [
        ('name_types',"UNIQUE(name)",'Property Types Must be Unique')
    ]
    