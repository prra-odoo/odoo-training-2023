# -*- coding: utf-8 -*-

from odoo import models , fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class estate_property(models.Model):
    _name = "estate.property"
    _description = "Advertisment module of real estate"
    active = fields.Boolean(default=True)
    
    
    name = fields.Char()
    postcode = fields.Integer(default = 104,readonly=True)
    description = fields.Text("Estate Property",copy=False)
    date_availability = fields.Date('Date Avilability',default=lambda self: fields.datetime.today()+relativedelta(months=6))
    expected_price = fields.Float(default = 550000)
    selling_price=fields.Float(default = 500000)
    bedrooms = fields.Integer(default = 50)
    living_area = fields.Integer(default = 2)
    facades = fields.Integer(default = 5)
    garage = fields.Boolean(default= False)
    garden_area = fields.Integer(default = 1)
    total_area = fields.Float(compute="_compute_total_area")
    best_offer =  fields.Float(compute= "_compute_offer_price",default=0)
    Other_info = fields.Text("Others info")
    log_note=fields.Text("Log Note")
    garage_orientation = fields.Selection(
        string = 'Garage_Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    state = fields.Selection(
        string='Type',
        selection=[('new','New'),('confirm','Confirm'),('done','Done'),('sold','Sold'),('cancel','Canceled')]
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property type")
    salesperson_id= fields.Many2one("res.partner",string="Sales")
    buyers_id=fields.Many2one("res.users",string="Buyers")
    tags_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer","property_id",string = "Property offer")\
    
    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
        
    @api.depends('offer_ids.price')
    def _compute_offer_price(self):
        for record in self:
            record.best_offer = max(self.offer_ids.mapped('price'))
            
            
    def action_sold(self):
        for record in self:
            if record.state == 'cancel':
                raise ValidationError("Canceled properties cannot be sold")
            else:
                 record.state == 'sold'
        return True
            
    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise ValidationError("Sold properties cannot be cannot be canceled")
            else:
                 record.state == 'cancel'
        return True