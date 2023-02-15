from odoo import api,models,fields
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate property advertisment'

    name = fields.Char(required=True, string='Title')
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char()
    expected_price = fields.Float(required=True)
    date_availability = fields.Date(copy=False, string='Available From', default=lambda self: fields.Date.today()+relativedelta(months=3))
    bedrooms = fields.Integer(default=2)
    facades = fields.Integer()
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    property_type_id = fields.Many2one('estate.property.type')
    buyer_id = fields.Many2one('res.partner', copy=False)
    seller_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    selling_price = fields.Float(readonly=True, copy=False)
    garage = fields.Boolean()
    state = fields.Selection(
        string = 'State', 
        default = 'offer received',
        selection = [('new','New'),('offer received','Offer Received'),('sold','Sold'),('canceled','Canceled')],
        help = 'Choose the direction',
        required = True,
        copy = False
    )
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    best_price = fields.Float(compute='_compute_best_price')
    total_area = fields.Integer(compute='_compute_total_area')
    living_area = fields.Integer()

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0

    garden = fields.Boolean(readonly=False)
    garden_direction= fields.Selection(
        readonly=False,
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        compute='_compute_garden',
        store=True)
    garden_area = fields.Integer(compute='_compute_garden', store=True, readonly=False)
    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if (record.garden==1):
                record.garden_direction = 'north'
                record.garden_area = 10
            else:
                record.garden_direction = ''
                record.garden_area = 0

    def action_button_sold(self):
        for record in self:
            if(record.state == 'canceled'):
                raise UserError('Canceled properties can not be sold.')
            else:
                record.state = 'sold'
        return True
    
    def action_button_cancel(self):
        for record in self:
            if(record.state == 'sold'):
                raise UserError('Sold properties can not be canceled.')
            else:
                record.state = 'canceled'
        return True
    
    

    