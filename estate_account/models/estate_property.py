from odoo import models

class InheritedModel(models.Model):
    _inherit = "estate.property"

    def inherited_action(self):
        return super().inherited_action()