from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import ValidationError,UserError 
from odoo.tools import float_utils


class estate_Property_offer(models.Model):
      _name = "estate.property.offer"
      _description = "Real estate based advertisedment module for the property type"
      _order='price desc'


      _sql_constraints = [    

      ('price', 'CHECK(price > 0)', 'Contained Quantity should be positive.'),

      ]
      price = fields.Float()
      status = fields.Selection(string='status',selection=[('Accepted','accepted'),('Refused','refused')],copy=False)
      partner_id = fields.Many2one("res.partner", string="Partner", required=True)
      property_id = fields.Many2one('estate.property',string="property id")      
      validity = fields.Integer(default='7')
      date_deadline = fields.Date( compute="_compute_date_deadline",inverse="_inverse_date_deadline")
      offer_ids = fields.One2many('estate.property.offer','property_type_id')
      property_type_id = fields.Many2one('estate.property.type',related='property_id.property_type_id',string='Property type', store=True)

      @api.depends('validity','date_deadline','create_date')
      def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.datetime.today()+ relativedelta(days=record.validity)

      def _inverse_date_deadline(self):
        for record in self:
         record.validity = (record.date_deadline - record.create_date.date()).days 

      def action_accepted(self):
            self.status = 'Accepted'
            # if float_compare(self.property_id.selling_price,(self.property_id.expeccted_price,)*90/100)<=0: 

            if self.property_id.selling_price <  ((self.property_id.expeccted_price) * 90)/100 and self.status == 'Accepted':
                    raise ValidationError("selling price must be 90 percentage of expected_price")
                    self.status='Refused'

            else:
                    self.property_id.selling_price = self.price
                    self.property_id.buyer_id = self.partner_id

            # if self.property_id 

      def action_refused(self):
          for record in self:
            self.status='Refused'
          return True

      '''the create method condition'''
      # @api.model
      # def create(self, vals):
      #   property_id = self.env['estate.property'].browse(vals['property_id'])
      #   max_price=max(property_id.offer_ids.mapped('price'),default=0)
      #   print(max_price)
      #   current_id = super().create(vals)
      #   if float_utils.float_compare(current_id.price,max_price,precision_digits=2) <= 0:
      #       raise ValidationError('The new offer must be greater than existing one')

      #   property_id.state = 'offer_received'
      #   return super().create(vals)
  
      @api.model
      def create(self, vals):
        property_id = self.env['estate.property'].browse(vals['property_id'])
        max_price = max(property_id.offer_ids.mapped('price'),default=0)
        print(max_price, vals.get('price'))
        if float_utils.float_compare(vals.get('price'),max_price,precision_digits=2) <= 0:
            raise ValidationError('The new offer must be greater than existing one')
        property_id.state = 'offer_received'
        return super().create(vals)



         