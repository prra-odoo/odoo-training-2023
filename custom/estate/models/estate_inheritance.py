from odoo import fields
from odoo import models
from dateutil.relativedelta import relativedelta


class EstateInheritance(models.Model):
    _name='estate.inheritance'
    _description="estate inheritance"
    # _inherit="estate.property"

    name = fields.Char(required=True, string="Title")
    postcode = fields.Char()
    dateavailability = fields.Date(copy=False, default=lambda self: fields.Date.today()+relativedelta(months=3))
