from odoo import models,fields

class TestOne(models.Model):
    _name = 'test.one'
    _description = 'test one'

    test_one_name = fields.Char()
    test_one_age = fields.Integer()