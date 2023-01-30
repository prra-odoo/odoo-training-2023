# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,_
from odoo.exceptions import AccessError

class RealEstateProperty(models.Model):
    _inherit =  "real.estate.property"
    
    def action_sold_porperty(self):
        print(self)
        res = super().action_sold_porperty()
        # if not self.env.user.has_group('real_estate.estate_group_manager'):
        #     raise AccessError(_("Do not have access, to sell the porperty"))
        print(self.env['account.move'].check_access_rights('write'), self.env['account.move'].check_access_rule('write'),"Security Rights")
        print(self.env['real.estate.property'].check_access_rights('write'),"write access rights")
        print(self.env['real.estate.property'].check_access_rule('write'),"Write Accesss rules")
        print(self.check_access_rights('write'),"Write Accesss rights")
        print(self.check_access_rule('write'),"Write Accesss rules")
        # print(self.check_access_rights('read'),"Read access rights")
        # print(self.check_access_rule('read'),"Read access rules")
        # print(self.check_access_rights('create'),"create access rights")
        # print(self.check_access_rule('create'),"create access rules")
        # print(self.check_access_rights('unlink'),"unlink Accesss Security")
        # print(self.check_access_rule('unlink'),"unlink Accesss rules")
        if self.env['account.move'].check_access_rights('write') and self.env['account.move'].check_access_rule('write'):
            for prop in self:
                print(prop.buyer_id.id)
                print(self.buyer_id.id)
                print(self.name)
                print(prop.name)
                self.env["account.move"].sudo().create(
                    {
                        "partner_id": self.buyer_id.id,
                        "move_type": "out_invoice",
                        "invoice_line_ids": [
                            (0,0,{
                                    "name": self.name,
                                    "quantity": 1.0,
                                    "price_unit": self.selling_price
                                },),
                            (0,0,{
                                    "name": "Administrative fees",
                                    "quantity": 1.0,
                                    "price_unit": 100.0,
                                },
                            ),],
                    }
                )
            print(res)
        return res
