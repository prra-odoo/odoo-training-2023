# -*- coding: utf-8 -*-
from odoo import api,fields,models

class realEstate(models.Model):
     _name = "real.estate"
     _description = "This is regarding the real_estate"

     name = fields.Char(string='Name',required = True)
     description = fields.Text(string='Description')
     postcode = fields.Integer(string='Postcode')
     date_availability = fields.Date(string='Date Available',default=lambda self: fields.Datetime.now())
     expected_price = fields.Float(string='Price',required = True)
     selling_price = fields.Float(string='Selling Price',required = True)
     bedrooms = fields.Integer(string='Bedrooms')
     living_area = fields.Integer(string='Living Area')
     facades = fields.Integer(string='Facades')
     garage = fields.Boolean(string='Garage')
     garden = fields.Boolean(string='Garden')
     garden_area = fields.Integer(string='Garden Area')
     property_type_id = fields.Many2one("estate.property.type", string="Property Type")
     salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user,copy=False) 
     buyer_id = fields.Many2one("res.partner", string="Buyer")
     garden_orientation = fields.Selection(
          selection =[('north', 'North'), ('south','South'),('east','East'),('west','West')]
     )
     tag_ids=fields.Many2many("estate.property.tag",string="Property Tags")
     offer_ids=fields.One2many("estate.property.offer", "property_id", string="Estate Offer")
     active = fields.Boolean(default = True)
     state = fields.Selection(selection = [('new', 'New'),
           ('offer_received', 'Offer Received'),
           ('offer_accepted', 'Offer Accepted'),
           ('sold', 'Sold'),('cancel','Cancelled')],default='new',required = True
           )
     total_area = fields.Integer(string='Total Area', compute="_compute_total")
     best_offer = fields.Float(string='Best Offer',compute="_compute_best_offer",default=0)
     
     @api.depends("living_area","garden_area")
     def _compute_total(self):
          for record in self:
               record.total_area= record.living_area + record.garden_area
     
     def _compute_best_offer(self):
          for record in self:
               record.best_offer = max(self.offer_ids.mapped('price'))

     