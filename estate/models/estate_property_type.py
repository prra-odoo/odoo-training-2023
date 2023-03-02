from odoo import fields,models,api
from odoo.exceptions import ValidationError

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate Property Type"
    _order="name"
    name=fields.Char(required=True)


    _sql_constraints=[
        ('unique_type','unique(name)','The Property type must be unique')
    ]



    property_ids=fields.One2many('estate.property','property_type_id')
    offer_ids=fields.One2many('estate.property.offer','property_type_id')
    offer_count=fields.Integer(compute="_compute_offer_count")


    @api.depends('offer_ids')
    def _compute_offer_count(self):
        if self.offer_ids:
            self.offer_count=self.env['estate.property.offer'].search_count([('property_type_id','=',self.id)])
        else:
            self.offer_count=0

                    # rec.places_owned=self.env['place.details'].search_count([('host_email','=',rec.email)])


        # for record in self:
        #    if record.offer_ids:
        #        record.offer_count=len(record.offer_ids)
        #        #record.offer_count=self.env['estate.property.offer'].search_count([])
        #    else:
        #        record.offer_count=0

    
                     
             
         
