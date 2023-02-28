from odoo import models,fields

class TestTwo(models.Model):
    _name = 'test.two'
    _inherits = {'test.one':'test_id'}
    _description = 'test two'

    test_two_name = fields.Char()
    test_two_age = fields.Integer()
    hello = fields.Char()
    test_id = fields.Many2one('test.one')