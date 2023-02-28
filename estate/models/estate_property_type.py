from odoo import models ,fields , api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "this is the Property Type Model"
    _order="sequence , name"
    name = fields.Char(required=True) 
    _sql_constraints=[
        ("check_type_name","UNIQUE(name)","The name must be unique")
    ]
    property_ids=fields.One2many("estate.property" ,"property_type_id")
    sequence=fields.Integer(string="Sequence" ,  default=1)

    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count=fields.Integer(compute="_compute_offer")

    @api.depends("offer_ids")
    def _compute_offer(self):
        for record in self:
            if record.offer_ids:
                record.offer_count=len(record.offer_ids)
            else:
                record.offer_count=0    
