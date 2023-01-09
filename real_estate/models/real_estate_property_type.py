from odoo import models, fields

class EstateType(models.Model):
    _name = "estate.property.type"
    _description = "This model will describe about type of houses"

    # creating a name field that will be stored in db
    name = fields.Char(string="Name", required=True)