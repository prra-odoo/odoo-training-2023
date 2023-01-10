from odoo import models

class EstateAccount(models.Model):
    _inherit = 'estate.property'

    def action_sold_button_header(self):
        print(".......................")
        return super(EstateAccount,self).action_sold_button_header()