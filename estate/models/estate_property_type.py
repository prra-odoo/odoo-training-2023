# -*- coding: utf-8 -*-

from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateModel(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"

    name = fields.Char('Name',required = True)
