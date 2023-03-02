from odoo import fields,models

class EstatePropertya(models.Model):
    _name="estate.property.prototype"
    _description="prototype inheriting from estate_property modela"
    _inherit="estate.property"

    rec = fields.Integer()
    