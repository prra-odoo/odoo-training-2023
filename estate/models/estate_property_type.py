from odoo import models,fields,api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real-estate property type"
    _order="name"
    _sql_constraints=[(
        'name_unique',
        'unique(name)',
        'Property Type name already exists')
    ]

    name = fields.Char(required=True)   
    property_ids= fields.One2many("estate.property","property_type_id")
    sequence=fields.Integer("Sequence",default="1",help="Used to order stages.Lower is better")    
    offer_ids=fields.One2many(
        comodel_name="estate.property.offer",
        inverse_name="property_type_id"
    )
    offer_count=fields.Integer(compute="_compute_offer_count")

    
    @api.depends('offer_ids') 
    def _compute_offer_count(self):
        for record in self:
            record.offer_count=len(record.offer_ids)   

   