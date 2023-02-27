from odoo import fields,models
class ModelTest(models.Model):
    _name="model.test"
    _description="prototype inheritance test"
    _rec_name="pro_name"
    pro_name=fields.Char()