from odoo import api,fields, models

class EstateProperty(models.Model):
    # _description = "estate property"
    _inherit="estate.property"

    def action_sold(self):

        print("hello")
        return super().action_sold()