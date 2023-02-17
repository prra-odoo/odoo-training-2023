from odoo import models,fields,api,exceptions

class EstatePropertyType(models.Model):
    
    _name = "estate.property.type"
    _description = "Property Type Model"
    _order = 'name asc'

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property","property_type_id")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")    
    _sql_constraints = [
          ('name_uniq', 'unique (name)', "Property type already exists !"),
       ]
    offer_ids = fields.One2many("estate.property.offers","property_type_id")
    offer_count = fields.Integer(compute="_compute_offers",store=True)

    # for counting the amount of offers received
    @api.constrains("offer_ids")
    def _compute_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    # for checking that property types are not similar like Flar,flat,fLat,FLat etc
    @api.constrains('name')
    def _check_unique_name(self):
        property_type_id = self.search([]) - self
        value = [x.name.lower() for x in property_type_id]
        if self.name and self.name.lower() in value:
            raise exceptions.ValidationError(('The combination is already Exist'))
        return True
