# -*- coding: utf-8 -*-
from odoo import models,fields
from dateutil.relativedelta import relativedelta


class estate_Property(models.Model):
      _name = "estate.property"
      _description = "Real estate based advertisedment module"

      name = fields.Char(required=True)  
      description = fields.Text()
      postcode = fields.Char()
      #date_availability=fields.Date(default=lambda self: fields.Date.today()+90)
      date_availability = fields.Date(default=lambda self: fields.Date.today() + relativedelta(months=+3), copy=False)
      expeccted_price=fields.Float()
      selling_price=fields.Float()
      bedroom=fields.Integer(default='2')
      living_area=fields.Integer()  #'deremo/estate_property_demo.xml',
      facades=fields.Integer()
      garage=fields.Boolean()
      garden=fields.Boolean()
      garden_area=fields.Integer()
      garden_orientation = fields.Selection(
        string='garden orientation',
        selection=[('north', 'North'), ('east', 'East'),('west', 'west'),('south', 'South')],
        help=("used for the garden orientation"))
      active = fields.Boolean('Active',default=True)
      state =fields.Selection(
        string='State',
        selection=[('New','new'),('Offer Received','offer received'),('Offer Accepted','offer accepted'),
        ('Sold','sold'),('Canceled','canceled')],
      )
      sales_id = fields.Many2one('estate.property.sales', string='Salesperson')
      buyer_id=fields.Many2one('estate.property.buyer', string='buyer')

      type_id=fields.Many2one('estate.property.type',string="product type")
      tag_ids=fields.Many2many(
       'estate.property.tag', string='Tags',
      help="Classify and analyze your lead/opportunity categories like: Training, Service")
      offer_ids= fields.One2many('estate.property.offer','property_id')







