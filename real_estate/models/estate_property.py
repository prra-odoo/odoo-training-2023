# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,models,fields

class EstateProperty(models.Model):
    _name="estate.properties"
    _description="Real estate properties"

    name=fields.Char('Property name',required=True)
    description=fields.Text('Property description')
    postcode=fields.Char('Postcode',required=True)
    date_availability=fields.Date('Date availability', copy=False)
    expected_price=fields.Float('expected price',required=True)
    selling_price=fields.Float('selling price',required=True, copy=False)
    bedrooms=fields.Integer('bedrooms', default=2)
    living_area=fields.Integer('living area')
    facades=fields.Integer('facades')
    garage=fields.Boolean('garage')
    garden=fields.Boolean('garden')
    garden_area=fields.Integer('garden area')
    type_id=fields.Many2one('estate.property.type', string='property type')
    garden_orientation = fields.Selection(string="Garden Orientation", selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active= fields.Boolean('active', default=True)
    state=fields.Selection(string="State",selection=[('new','New'),('offer_received','Offer received'),('offer_accepted','Offer accepted'),('sold','Sold'),('canceled','Canceled')],default='new',required=True)
    buyer_id=fields.Many2one('res.partner', copy=False, string='user')
    salesperson_id=fields.Many2one('res.users', string='salesperson', default=lambda self: self.env.user)
    tag_ids=fields.Many2many('estate.property.tags', string='property tags')
    offer_ids=fields.One2many("estate.property.offer","property_id", string="Offers")
    total_area=fields.Float(compute="_compute_total_area",)
    best_offer=fields.Float(compute="_compute_best_offer")

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer=max(record.offer_ids.mapped('price'),default=0)


