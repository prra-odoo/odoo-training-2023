# -*- coding: utf-8 -*-


from odoo import models, fields
from odoo.tools.date_utils import add


class realEstate(models.Model):
    _name = "estate.property"
    _description = "This is the Database for the all clients and their requirements"

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Post Code")
    date_availability = fields.Date( "Available From", default=add(fields.Datetime.now(), months=3))
    expected_price = fields.Float("Excepted Price")
    selling_price = fields.Float("Selling Price")
    bedrooms = fields.Integer("Bedrooms")
    living_area = fields.Integer("Living Area", default="1")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        selection=[('small', 'Small'), ('big', 'Big')]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'), 
            ('offer_received', 'Offer Received'), 
            ('offer_accepted', 'Offer Accepted'), 
            ('sold', 'Sold'), 
            ('canceled', 'Canceled')],default="new"
    )   
