# -*- coding: utf-8 -*-
from odoo import models,fields
from dateutil.relativedelta import relativedelta
from odoo import api
from odoo.exceptions import UserError

class estate_Property(models.Model):
      _name = "estate.property"
      _description = "Real estate based advertisedment module"
      _inherit = ['mail.thread','mail.activity.mixin']
      _order = "id desc"

      _sql_constraints = [                                                                                    
    
        ('name', 'unique(name)', "A name can only be assigned to one product !"),
        ('expeccted_price', 'CHECK(expeccted_price > 0)', 'Contained Quantity should be positive.'),
        ('selling_price', 'CHECK(selling_price > 0)', 'Contained Quantity should be positive.'),
                                                                                           
      ]
      
      name = fields.Char(required=True)  
      description = fields.Text()
      postcode = fields.Char()
      date_availability = fields.Date(default=lambda self: fields.Date.today() + relativedelta(months=+3), copy=False)
      expeccted_price=fields.Float()
      selling_price=fields.Float()
      bedroom=fields.Integer(default='2')
      living_area=fields.Integer()  #'deremo/estate_property_demo.xml',
      facades=fields.Integer()
      garage=fields.Boolean()
      garden=fields.Boolean()
      garden_area=fields.Integer(compute='_compute_garden')
      garden_orientation = fields.Selection(
        string='garden orientation',
        selection=[('north', 'North'), ('east', 'East'),('west', 'west'),('south', 'South')],
        help=("used for the garden orientation"))
      active = fields.Boolean('Active',default=True)
      state=fields.Selection(string='status',selection=[('new' , 'New'),('offer_received','Offer_Received'),('offer_accepted','Offer_Accepted'),('sold' , 'Sold'),('canceled' , 'Canceled')],tracking=True,default='new')
      sales_id = fields.Many2one('res.users', string='Salesperson')
      buyer_id=fields.Many2one('res.partner', string='buyer')
      type_id=fields.Many2one('estate.property.type',string="product type")    
      tag_ids=fields.Many2many(
       'estate.property.tag', string='Tags',
      help="Classify and analyze your lead/opportunity categories like: Training, Service")
      offer_ids= fields.One2many('estate.property.offer','property_id')
      property_type_id=fields.Many2one('estate.property.type')
      total_area=fields.Float(compute='_compute_total_area')
      best_price=fields.Float(compute='_compute_best_price')
      company_id = fields.Many2one(
        'res.company', required=True, default=lambda self: self.env.company
    )


      @api.depends('living_area', 'garden_area')
      def _compute_total_area(self):
        for rec in self:
          rec.total_area = rec.living_area+rec.garden_area
     
      @api.depends('offer_ids.price')
      def _compute_best_price(self):
          for record in self:
            record.best_price = max(self.offer_ids.mapped('price'),default=0)

    
      def sold_action(self):
        for record in self: #self --> recordset/collection --> gives record one by one
            if record.state == 'canceled':
                raise UserError('Canceled property can not be sold.')
            else:    
                record.state = 'sold'
        return True
       
      def canceled_action(self):
        for record in self:
          if record.state == 'sold':
            raise UserError('sold  property can not be canceled')
                  
          else:
            record.state = 'canceled'
        return True
      
      @api.ondelete(at_uninstall=False)
      def _ondeleteaction(self):
        for record in self:
          if record.state in ('offer_received','offer_accepted','sold'):
            raise UserError("only delete a property with the new and canceled state")

      @api.depends('garden')
      def _compute_garden(self):
        for record in self:
          if record.garden == True:
            record.garden_area = 10
            record.garden_orientation ='north'
          else:
            record.garden_area=0
            record.garden_orientation=False
            


        
      



       
      

       
       


        
       

          
 
      
       
        







