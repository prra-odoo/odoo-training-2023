from  odoo import fields,models
class EstateProto(models.Model):
    _name="estate.proto"
    _description="Just Prototype"

    p_price=fields.Float()
    p_date=fields.Date()
    p_postcode=fields.Char()
