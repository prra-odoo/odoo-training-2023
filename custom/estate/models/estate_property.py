from odoo import api,models,fields
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from odoo.tools import float_is_zero, float_compare

class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'estate property advertisment'
    _order = 'id desc'

    name = fields.Char(required=True, string='Title')
    number = fields.Char(string='Property No.',default=lambda self: ('New'))
    active = fields.Boolean(default=True)
    description = fields.Text()
    image = fields.Binary()
    postcode = fields.Char()
    expected_price = fields.Float()
    date_availability = fields.Date(copy=False, string='Available From', default=lambda self: fields.Date.today()+relativedelta(months=3))
    bedrooms = fields.Integer(default=2)
    facades = fields.Integer()
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    property_type_id = fields.Many2one('estate.property.type')
    buyer_id = fields.Many2one('res.partner', copy=False)
    seller_id = fields.Many2one('res.users', default=lambda self: self.env.user.id)
    selling_price = fields.Float()
    garage = fields.Boolean()
    state = fields.Selection(
        string = 'State', 
        default = 'new',
        selection = [('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        help = 'Choose the direction',
        copy = False,
        tracking = True,
    )
    kanbancolor = fields.Integer('Color Index', compute='set_kanban_color')
    priority = fields.Selection([('0', 'Low'),('1', 'High')])
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    best_price = fields.Float(compute='_compute_best_price')
    total_area = fields.Integer(compute='_compute_total_area')
    living_area = fields.Integer()
    garden = fields.Boolean(readonly=False)
    garden_orientation= fields.Selection(
        readonly=False,
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        compute='_compute_garden',
        store=True)
    garden_area = fields.Integer(compute='_compute_garden', store=True, readonly=False)

    _sql_constraints = [
        ('check_expected_price','CHECK(expected_price >= 0)','The expected price cannot be negative.'),
        ('check_selling_price','CHECK(selling_price >= 0)','The selling price cannot be negative.'),
    ]

    @api.model
    def create(self,vals):
        vals['number'] = self.env['ir.sequence'].next_by_code('estate.property')
        return super(EstateProperty,self).create(vals)

    def unlink(self):
        for record in self:
            if(record.state not in ('new','canceled')):
                raise UserError('Only new and canceled properties can be delete')
        return super().unlink()
    
    # @api.ondelete(at_uninstall=False)
    # def prevent_delete(self):
    #     for record in self:
    #         if (record.state not in ('new','canceled')):
    #             raise UserError('Only new and canceled properties can be delete')

    def set_kanban_color(self):
        for record in self:
            if record.state == 'new':
                kanbancolor = 0
            elif record.state == 'offer received':
                kanbancolor = 10
            elif record.state == 'offer accepted':
                kanbancolor = 10
            elif record.state == 'sold':
                kanbancolor = 4
            else:
                kanbancolor = 9
            record.kanbancolor = kanbancolor 

    @api.constrains('selling_price','expected_price')
    def _check_selling_price(self):
        for record in self:
            sp = (90 * record.expected_price) / 100
            if(not float_is_zero(record.selling_price, precision_rounding=0.01)):
                if (float_compare(sp,record.selling_price, precision_rounding=0.01) >= 0):
                    raise ValidationError('The selling price must be at least 90% of the expected price! You must reduce the expected price if you want to accept this offer.')

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'),default=0)

    @api.depends('garden')
    def _compute_garden(self):
        for record in self:
            if (record.garden==1):
                record.garden_orientation = 'north'
                record.garden_area = 10
            else:
                record.garden_orientation = ''
                record.garden_area = 0

    def action_sold(self):
        for record in self:
            print('estate property')
            # if(record.state == 'canceled'):
            #     raise UserError('Canceled properties can not be sold.')
            # else:
            #     record.state = 'sold'
            record.state = 'sold'
        return True
    
    def action_cancel(self):
        for record in self:
        #     if(record.state == 'sold'):
        #         raise UserError('Sold properties can not be canceled.')
        #     else:
            record.state = 'canceled'
        return True