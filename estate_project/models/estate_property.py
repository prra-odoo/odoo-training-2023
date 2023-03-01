from odoo import models, fields, api


class EstateProperty(models.Model):
    _inherit = ["estate.property"]

    def btn_sold(self):

        return super().btn_sold()
