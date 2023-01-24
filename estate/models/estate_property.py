# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.tools.date_utils import add
from odoo.exceptions import UserError,ValidationError
from odoo.tools.float_utils import float_compare



class estatePropertyModel(models.Model):
    _name = "estate.property"
    _description = "Esate property model"
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name:', required=True)
    postcode = fields.Char()
    description = fields.Text()
    date_availability = fields.Date(
        'Date availability', default=lambda self: fields.datetime.now()+relativedelta(months=3))
    # + relativedelta(months=6)+relativedelta(days=5)
    sold_date = fields.Date('Selling date')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living area', copy=False)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')],
    )
    total_area = fields.Float(compute="_total_area")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('new', 'New'), ('offer_recieved',
                                    'Offer recieved'), ('offer_accepted', 'Offer accepted'),('sold','Sold'),('cancelled','Cancelled')],
        default='new', string ="Status", tracking=True
    )

    property_type_id = fields.Many2one("estate.property.type", string="Type")
    salesperson_id = fields.Many2one(
        "res.users", string="Salesperson", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyers", copy=False)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many(
        'estate.property.offer', 'property_id', string="offers")
    best_offers = fields.Float(compute="_best_offer" , default =0)

    

    # listing_property = fields.Many2one('estate.property.type')

    @api.depends("living_area", "garden_area")
    def _total_area(self):
        for record in self:
            record.total_area = record.living_area+record.garden_area

    @api.depends("offer_ids.price", "offer_ids.status")
    def _best_offer(self):
        for record in self:
            record.best_offers = max(record.offer_ids.mapped('price'),default=0)
            
                
    def sold_product(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError("Cancelled properties cannot be sold")
            else:
                record.state = 'sold'
        
    def cancelled_product(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold Properties cannot cancelled")
            else:
                record.state='cancelled'
            
    _sql_constraints=[
        ('check_selling_price' , 'CHECK(selling_price>=0)',
        'Selling price must be positive'),
        (
             'check_expected_price' , 'CHECK(expected_price>=0)',
             'Expected Price must be Positive'
        )
    ]
    # Adding the python constraints so that the selling 
    @api.constrains("selling_price","expected_price")
    def _check_selling_price(self):
        for record in self:
            if  float_compare(record.selling_price,0.9*record.expected_price,precision_digits =2) == -1:
                raise UserError("Selling Price must 90percent of the expected price")




           
    @api.ondelete(at_uninstall=False)
    def _deleting_the_record(self):
        for record in self:
            if record.state == 'offer_recieved' or record.state =='offer_accepted' or record.state=="done":
                raise ValidationError("you can delete the record in new or cancelled stage")

        
        
    


                   

