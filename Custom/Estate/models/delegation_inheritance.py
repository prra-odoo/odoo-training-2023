from odoo import fields,models

class EstateDelegation(models.Model):
    _name="estate.deligation.test"
    _inherits = {'estate.property':'estate_delig'}
    _description="creating a deligation inheritance for testing with estate_property"

    estate_delig_id = fields.Many2one('estate.property',required=True)
    read = fields.Char()