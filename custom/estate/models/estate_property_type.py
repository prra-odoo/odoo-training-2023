from odoo import models,fields,api
class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Property Type must be unique'),
    ]
    _order="sequence , name"


    name=fields.Char()
    property_ids=fields.One2many('estate.real.property','property_type_id',string="types")
    sequence=fields.Integer(default=1)
    offer_ids=fields.One2many('estate.property.offer','property_type_id')
    offer_count=fields.Integer(compute="_compute_offer_count")
    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            """ record.offer_count = self.env['estate.property.offer'].search_count([('property_type_id.name','=','record.name')])
 """             
            record.offer_count=len(record.offer_ids)
                
             

