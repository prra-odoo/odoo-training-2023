# -*- coding: utf-8 -*-
from odoo import fields, models, exceptions


class estate_property(models.Model):

    _inherit = "estate.property"

    def action_sold(self):
        print('this is working')
        self.env['account.move'].create(
            {
                "partner_id": self.buyer_id,
                "move_type": "out_invoice",
            }
        )              
        return super().action_sold()
