from odoo import fields,models

class estateProperty(models.Model):
    _name = "estate.property"
    _description="model description"

    id=fields.Integer()
    create_uid=fields.Integer()
    create_date=fields.Date()
    write_uid=fields.Integer()
    write_date=fields.Date()
    name=fields.Char()
    description=fields.Char()
    