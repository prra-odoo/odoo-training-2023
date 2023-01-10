from odoo import models,fields,api
from dateutil.relativedelta import relativedelta


class estate_Property_offer(models.Model):
      _name = "estate.property.offer"
      _description = "Real estate based advertisedment module for the property type"

      price = fields.Float()
      status = fields.Selection(string='status',selection=[('Accepted','accepted'),('Refused','refused')],copy=False)
      partner_id = fields.Many2one("res.partner", string="Partner", required=True)
      property_id = fields.Many2one('estate.property',string="property id")
      validity = fields.Integer(default='7')
      date_deadline = fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")
      @api.depends('validity','date_deadline','create_date')
      def _compute_date_deadline(self):
            for record in self:
                  if record.create_date:
                   record.date_deadline = fields.Datetime.now() + relativedelta(days=record.validity)
                  else:
                   record.date_deadline = fields.Datetime.now() + relativedelta(days=record.validity)
      
      def _inverse_date_deadline(self):
             for record in self:
                  record.date_deadline = fields.Datetime.now() - relativedelta(days=record.validity).days
                   
      

fields.Date.today() + relativedelta(months=+3)
