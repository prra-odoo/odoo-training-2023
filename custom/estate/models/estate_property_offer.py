from odoo import api,models,fields, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate property offer'
    _order = 'price desc'

    price = fields.Float()
    status = fields.Selection(
        selection = [('accepted','Accepted'),('refused','Refused')],
        copy = False,
        required=False
    )
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('estate.property')
    validity = fields.Integer(default=7, string='Validity (days)')
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)

    _sql_constraints = [
        (
            'check_price','CHECK(price >= 0.0)','The offer price cannot be negative.'
        )
    ]

    @api.model
    def create(self, vals_list):
        record = self.env['estate.property'].browse(vals_list['property_id'])
        print(record)
        record.state = 'offer received'
        if((vals_list['price']) <= record.best_price):
            higher_price = int(record.best_price)
            raise UserError(_('Offer must be higher than %s', higher_price))
        return super().create(vals_list)

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if (record.create_date):
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days

    def action_accept(self):
        for record in self.property_id.offer_ids:
            record.status = 'refused'   
        self.property_id.state = 'offer accepted'
        self.property_id.selling_price = self.price     
        self.property_id.buyer_id = self.partner_id
        self.status = 'accepted'
        return True     
    
    def action_refuse(self):
        for record in self:
            if(record.status == 'accepted'):
                self.property_id.state = 'offer received'
                self.property_id.selling_price = 0
                self.property_id.buyer_id = ''
        record.status = 'refused'
        return True