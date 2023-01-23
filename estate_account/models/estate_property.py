from odoo import fields,api,models

class Inherited_estate_property(models.Model):
    _inherit="estate.property.model"

    name=fields.Char(required=True)

    def perform_sold(self):
        print("Inherited Function in estate account being called")
        return super().perform_sold()

