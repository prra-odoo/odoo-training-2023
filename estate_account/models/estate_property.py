from odoo import fields, models, api

class InheritedEstateProperty(models.Model):
    # _name="estate.property.inherit"
    _inherit="estate.property"

    def action_set_sold(self):
        print("Inherited Estate Property")
        return super(InheritedEstateProperty,self).action_set_sold()