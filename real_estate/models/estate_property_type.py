from odoo import fields, models, api

class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _order = "name"

    name = fields.Char('Name', required = True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer('Sequence', default=1)

    offer_ids = fields.One2many('estate.property.offer','property_type_id', string="Offers")
    offer_count = fields.Integer('Offer Count', compute= '_count_offer') 

    

    _sql_constraints = [
            ('name_uniq', 'unique (name)', "Property Type already exists !"),
    ]

    @api.depends('offer_ids')
    def _count_offer(self):
        for record in self:
                record.offer_count = len(record.offer_ids)