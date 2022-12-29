# -*- coding: utf-8 -*-

from odoo import models, fields


class TestModel(models.Model):
    __name = "test.model"

    name = fields.Char(string="Expected Price", required=True)
    expected_price = fields.Float(string="Expected Price", required=True)


