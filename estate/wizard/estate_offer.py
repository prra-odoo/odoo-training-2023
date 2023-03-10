# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class EstateOffer(models.TransientModel):
    _name = "estate.offer"
    _description = "Apply offers to multiple properties at once."

    name = fields.Char()
