# -*- coding:utf:8 -*-

from odoo import models, fields, api
from odoo.tools.date_utils import add
from odoo.exceptions import UserError, ValidationError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Offer module"
    _order = "price desc"

    price = fields.Float("Price")

    validity = fields.Integer()
    
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])

    date_deadline = fields.Date(
        "Date Deadline", compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    create_date = fields.Date(default=fields.Datetime.now(), readonly=True)

    #Relations Fields
    property_type_id = fields.Many2one('estate.property.type')
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)

    #SQL Constraints
    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0)',
         'UserError : Enter the Validate Price')
    ]

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        """
        Compute perform user add valiidaty and directly
        impact on date_deadlie field with current date
        """
        for record in self:
            record.date_deadline = add(
                record.create_date, days=record.validity)

    def _inverse_date_deadline(self):
        """
        Inverse perform reverse of @_compute_date_deadline function
        """
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline -
                                   record.create_date).days

    @api.depends("property_id.buyer_id", "property.selling_price", "property_id.state")
    def action_accept(self):
        """
        In action_accept(button),for creating function user
        accepted offer 
        """
        if self.property_id.selling_price == 0:
            self.property_id.selling_price = self.price
            self.property_id.buyer_id = self.partner_id
            self.status = "accepted"
            self.property_id.state = "offer_accepted"

    def action_refuse(self):
        """
        In action_refuse(button),for creating function
        other offer refuse  automatically  
        """
        self.status = 'refused'
        self.property_id.selling_price = 0
        self.property_id.state = "new"

    #Create Method 
        """
        This method call when user creating one offer and enter the price amount 
        check the condition price must be higer than previous price otherwise getting
        User error
        """
    @api.model
    def create(self, vals):
        domain = ['property_id', '=', vals['property_id']]
        result = self.env['estate.property.offer'].search(
            [domain]).mapped('price')
        for record in result:
            if vals['price'] < record:
                raise UserError("Increasing Your Amount")
        self.env['estate.property'].browse(
            vals['property_id']).state = "offer_received"
        return super().create(vals)
