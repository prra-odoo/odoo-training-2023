from odoo import api,models,fields

class EstateTypeProperty(models.Model):
    _name="real.estate.property.type"
    _description="Property Type Model"
    _order="name"

    name=fields.Char(string="name",required=True)
    description=fields.Text('Description')
    property_ids=fields.One2many('real.estate.properties','type_id')
    sequence=fields.Integer('Sequence',default=1,help="Use to order stages.")
    offer_ids=fields.One2many('real.estate.property.offer','property_type_id')
    offer_count=fields.Integer(compute='_compute_offer_count')


    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count=len(record.offer_ids)

    _sql_constraints = [
        ('name', 'unique(name)', "A Type with the same name already exists."),
    ]


