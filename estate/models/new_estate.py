# -*- coding: utf-8 -*-
from odoo import models, fields


class NewEstate(models.Model):
    _name = "new.estate"
    _description = "new estate Model"

    n_postcode = fields.Char()
    n_date = fields.Date()
    n_price = fields.Float()
