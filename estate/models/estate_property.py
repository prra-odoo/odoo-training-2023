# -*- coding: utf-8 -*-

from odoo import models,fields
from dateutil.relativedelta import relativedelta
# from odoo.tools.date_utils import add

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property module "

    name = fields.Char(required=True)
    id = fields.Integer()
    postcode = fields.Char()
    description = fields.Text(copy=False)
    property_type_id=fields.Many2one("estate.property.type",string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesman_id = fields.Many2one('res.users', string='Salesman')
    # tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    date_availability = fields.Date('Date Avilability',default=lambda self: fields.datetime.today()+relativedelta(months=3))
    # date_avilability = fields.Date('Date Avilability',default=lambda self:add(fields.datetime.today(),months=3))
    expected_price = fields.Float("Expected Price")
    selling_price = fields.Float("Selling Price",readonly=True,default=2000000)
    bedrooms = fields.Integer(default=3)
    living_area = fields.Integer("Lving Area")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer("Garden Area")
    other_info=fields.Text('Other Info')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    state = fields.Selection( 
        string='State', 
    selection = [('new', 'New'),('in_progress', 'In Progress'),('cancel', 'Cancelled'),('done', 'Done')])

