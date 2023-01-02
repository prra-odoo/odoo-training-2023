#-*- coding:utf:8 -*- 

from odoo import models,fields  

class estatePropertyOffer(models.Model): 
     _name = "estate.property.offer"
     # real.estate
     _description = "Real Estate offer module" 


     # o_name=fields.Char()
     # description = fields.Text(string='Description')
     price = fields.Float()
     status= fields.Selection(
          selection=[('accepted','Accepted'),('refused', 'Refused')]   
          )
     partner_id=fields.Many2one('res.partner')
     property_id=fields.Many2one('estate.property')
