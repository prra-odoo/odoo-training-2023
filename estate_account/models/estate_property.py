# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo import Command
from odoo.exceptions import ValidationError, UserError


class EstateProperty(models.Model):
    _inherit = "estate.property"

    name = fields.Char()

    # def action_sold(self):
    #     # res = super.action_sold()
    #     if self.state == 'sold':
    #         self.env.ref('account_accountant.account.move').trigger()
    #         raise UserError("nothing workung ")
    #     return True

    # print(action_sold)
