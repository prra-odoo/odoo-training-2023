# -*- coding: utf-8 -*-
from odoo import models


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sold_action(self):
        for record in self:
        # print('overwrite successfully')
            self.env["account.move"].create({
                'partner_id': record.buyer_id.id,
                'move_type':  'out_invoice'
            })
        return super().sold_action()