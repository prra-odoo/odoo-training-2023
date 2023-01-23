# -*- coding: utf-8 -*-

from odoo import models,_,fields , api
from dateutil.relativedelta import relativedelta
from odoo.tools.date_utils import add,subtract
from odoo.exceptions import ValidationError,UserError
from odoo.tools.float_utils import float_compare

class estateOffer(models.Model):
    _name="estate.property.offer"
    _description = "This is the estate property offer model"
    _order = "price desc"
    _sql_constraints=[
       ( ('check_price'),'CHECK(price>0)','The offer price must be have some value')
    ]

    price = fields.Float()
    status = fields.Selection(string = "status",selection = [('accepted','Accepted'),('refused','Refused')])
    create_date = fields.Date(default = lambda self: fields.datetime.today(),readonly=True)
    validity = fields.Integer("Validity",default=7)
    date_deadline = fields.Date("Deadline" ,compute="_compute_deadline_" , inverse = "_compute_validty_changes_")
    partner_id = fields.Many2one("res.partner",string="Partner id",)
    property_id= fields.Many2one("estate.property",string="Property id")
    property_type_id = fields.Many2one("estate.property.type",related = "property_id.property_type_id",store=True,string="Property Type")
    
    @api.depends('create_date','validity','date_deadline')
    def _compute_deadline_(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta( days =+ record.validity)
            
    def _compute_validty_changes_(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    
    
    def action_accept(self):
        for record in self.search([('status','=','accepted')]):
            if record.property_id == self.property_id:
                raise ValidationError("Can't accept more than one")
            else:
                for i in record:
                    record.status='refused'
        self.status='accepted'
        self.property_id.state='offer_accepted'
        self.property_id.selling_price = self.price
        self.property_id.buyers_id = self.partner_id


    def action_refused(self):
        for record in self:
            record.status = 'refused'
            
    @api.model
    def create(self,vals):
        record = self.env['estate.property'].browse(vals['property_id']) 
        if record.offer_ids['price']:
            max_price = max(record.mapped('offer_ids.price'))
            if float_compare(vals['price'],max_price,precision_rounding=0.01) <=0:
                raise UserError("The offer price must be higher than %.2f" % max_price)
        record.state = 'offer_received'
        return super().create(vals)         
    
            
   
        
        
    
  
                
        
            
            
            
    
            
    