from odoo import models , fields,api
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer (models.Model):
   _name="estate.property.offer"
   _description="This is a property offer model"
   _order="price desc"

   price = fields.Float(string="Price")
   status = fields.Selection(string='Status',
      selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
      help="status is used to show offer status",copy=False)
   partner_id = fields.Many2one('res.partner',required=True)
   property_id=fields.Many2one('estate.property',required=True)
   validity=fields.Integer(default=7) 
   date_deadline=fields.Date(compute="_compute_date_deadline" , inverse="_inverse_date_deadline")

   @api.depends("validity", "create_date")
   def _compute_date_deadline(self):
      for record in self:  
         if record.create_date:
            record.date_deadline=record.create_date + relativedelta(days=record.validity)
         else:
            record.date_deadline=fields.Date.today() + relativedelta(days=record.validity)
   @api.depends("date_deadline" , "create_date") #nothing meaning of writing this bcoz inverse triggerd once the record is save
   def _inverse_date_deadline(self):
      for record in self:
         record.validity = (record.date_deadline-record.create_date.date()).days

   def action_accepted(self):
      for record in self.property_id.offer_ids:
            record.status = 'refused'
      self.status = 'accepted'
      self.property_id.selling_price = self.price
      self.property_id.buyer = self.partner_id
      self.property_id.state = 'offer_accepted'

   def action_refused(self):
      for record in self:
         record.status="refused"