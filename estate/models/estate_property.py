# -*- coding: utf-8 -*-

from odoo import models , fields

class test(models.Model):
    _name = "estate.property"
    _description = "Advertisment module of real estate"
    
    
    name = fields.Char(required = True)
    postcode = fields.Integer(default = 104,readonly=True)
    description = fields.Text("Estate Property",required = True,copy=False)
    date_availability = fields.Date("Last Availability Date",default=lambda self:fields.Datetime.now())
    expected_price = fields.Float(default = 550000)
    selling_price=fields.Float(default = 500000)
    bedrooms = fields.Integer(default = 50)
    living_area = fields.Integer(default = 2)
    facades = fields.Integer(default = 5)
    garage = fields.Boolean(default= False)
    garden_area = fields.Integer(default = 1)
    Other_info = fields.Text("Others info",required=True)
    log_note=fields.Text("Log Note")
    garage_orientation = fields.Selection(
        string = 'Garage_Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    state = fields.Selection(
        string='Type',
        selection=[('new','New'),('confirm','Confirm'),('done','Done')]
    )
    active = fields.Boolean(default=True)
    
    
     