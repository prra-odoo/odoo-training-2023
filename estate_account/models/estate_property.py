from odoo import fields, models

class InheritedEstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_click(self):
        
        print("The parent method is called from the child class")
        super().sold_click()