# -*- coding: utf-8 -*-
from odoo import api,fields, models
from odoo.exceptions import UserError


class estateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Model"

    name = fields.Char('Name', required = True)
    description = fields.Text('Description')
    postcode = fields.Integer('Postcode' ,required= True)
    date_availability = fields.Date('Date', default=lambda self: fields.Datetime.now(), readonly=True)
    expected_price = fields.Float('Expected price')
    selling_price = fields.Float('Seling price' , default = '20000', copy = False)
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden area', default = "2500")
    total_area = fields.Integer('Total Area', compute="_compute_total_area")
    best_price = fields.Integer('Best Price', compute="_compute_best_price")
    status = fields.Char('Status', readonly=True, default="New")
    garden_orientation = fields.Selection(string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('west', 'West'), ('east', 'East')],
        help="Type is used to separate Leads and Opportunities")
    state = fields.Selection(string = "state", selection = [('new', 'New'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default= "new")
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesman_id = fields.Many2one("res.users", string="Salesman" ,default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyers")
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer","property_id")

   
    @api.depends("garden_area","living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            # for rec in record.offer_ids:
            #     if rec.status == 'accepted':
            #         record.best_price = max(rec.mapped('price'), default=0)
            #     elif rec.status == 'refused':
            #         continue
            #     else:
            #         record.best_price = 0
            # if record.offer_ids.status == 'refused':
            #     record.best_price = 0
            record.best_price = max(record.offer_ids.mapped('price'), default=0)

    def action_sold(self):
        for record in self:
            if record.status == 'Canceled':
                raise UserError('Canceled Property cannot be sold.')
            else:
                record.status = "Sold"
        return True
    
    def action_cancel(self):
        for record in self:
            if record.status == 'Sold':
                raise UserError('Sold Property cannot be canceled.')
            else:
                record.status = "Canceled"
        return True
    
   