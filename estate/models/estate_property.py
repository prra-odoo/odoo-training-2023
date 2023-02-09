# -*- coding: utf-8 -*-
from odoo import api,fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name="estate.property"
    _description="Estate Property Description"
    
    name = fields.Char(required=True,string="Title")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=lambda self: fields.Date.today()+relativedelta(months=3),string="Available From")
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean(default=True)
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[('north',"North"),('south',"South"),('east',"East"),('west',"West")]
    )
    active = fields.Boolean(default=True,required=True)
    state = fields.Selection(
        string="State",
        required=True,
        selection=[('new',"New"),('offer_received',"Offer Received"),('offer_accepted',"Offer Accepted"),('sold',"Sold"),('cancelled',"Cancelled")],
        default='new'
    )
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")
    buyer = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesperson = fields.Many2one("res.users",string="Salesman",default= lambda self : self.env.user)
    tag_ids = fields.Many2many("estate.property.tag",string="Tags")
    offer_ids = fields.One2many("estate.property.offer","property_id",string="Offers")
    total_area = fields.Integer(compute="_compute_total_area")
    best_offer = fields.Float(compute="_compute_best_offer")

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.living_area+record.garden_area


    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            if(record.offer_ids):
                record.best_offer=max(record.offer_ids.mapped("price"))
            else:
                record.best_offer=0.0

    @api.onchange("garden")
    def _onchange_garden(self):
        if(self.garden==True):
            self.garden_area=10
            self.garden_orientation="north"

        else:
            self.garden_area = 0
            self.garden_orientation=""