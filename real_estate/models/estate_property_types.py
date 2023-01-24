from odoo import fields,models,api

class Property_type(models.Model):
    _name = "estate.property.type"
    _description = "Estate property types"
    _order = "name"

    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence')
    property_ids = fields.One2many("estate.property.model","type_id",readonly=True)
    offer_ids = fields.One2many("estate.property.offer","property_type_id")
    offer_count = fields.Integer(compute="_compute_tot_offer")

    @api.depends('offer_ids')
    def _compute_tot_offer(self):
        
         for record in self:
            record.offer_count=len(record.offer_ids)
        
        

    _sql_constraints = [
        ('unique_type_name','unique(name)','Type name must be unique'),
    ]
    



