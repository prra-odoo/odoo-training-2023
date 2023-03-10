from odoo import api,fields, models,exceptions,tools
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"
    _order = "id desc"
    _sql_constraints = [
        ('check_expected_price','CHECK(expected_price>0)','The expected price must be strictly positive.'),
    ]
    _inherit = ['estate.prototype','mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description = fields.Text()
    postcode = fields.Char() 
    date_availability = fields.Date(copy=False,default=lambda self: fields.Datetime.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(readonly = False, store = True)
    garden_orientation = fields.Selection(
        readonly = False,
        string='Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Type is used to separate Leads and Opportunities",
        store = True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer received', 'Offer Received'), 
        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required=True,copy=False,tracking = True)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson",default=lambda self:self.env.user)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags", relation="tag_ids_m2m")
    offer_ids = fields.One2many("estate.property.offer","property_id", string="Offers")
    image = fields.Binary()

    total_area = fields.Float(compute="_compute_total_area")
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            if (record.garden==True):
                record.total_area = record.living_area + record.garden_area
            else:
                record.total_area = record.living_area

    best_price = fields.Float(compute="_compute_best_price",store=True)
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            if(record.offer_ids):
                # if(record.state == "new"):
                #     record.state = "offer received"
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0.0

            # if(record.state == "offer received"):
            #     if(not record.offer_ids):
            #         record.state = "new"

    # @api.depends('garden')
    # def _compute_garden_values(self):
    #     for record in self:
    #         if (record.garden == True):
    #             record.garden_area = 10
    #             record.garden_orientation = 'north'
            
    #         else:
    #             record.garden_area = 0
    #             record.garden_orientation = ''
    
    color = fields.Integer(compute="_compute_color")     
    @api.depends('state')
    def _compute_color(self):
        for record in self:
            if(record.state == 'offer accepted'):
                record.color = 10
            elif(record.state == 'offer received'):
                record.color = 4
            elif(record.state == 'new'):
                record.color = 3
            else:
                record.color = 1
       
    def action_sold(self):
        for record in self:
            record.state = 'sold'
            # if record.state == 'cancelled':
            #     raise exceptions.UserError("Cancelled properties cannot be sold.")
            # else: record.state = 'sold'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
            # if record.state == 'sold':
            #     raise exceptions.UserError("Sold properties cannot be cancelled.")
            # else:record.state = 'cancelled'

    # now to check that the selling price is not less than 90% of its expected price
    #    -1 : If the first value is less than the second value.
    #    0 : If the first value is equal to the second value.
    #    1 : If the first value is greater than the second value.

    # @api.constrains('expected_price')
    # def _selling_price(self):
    #     for record in self:
    #         if not float_is_zero(record.expected_price, precision_digits=2) and not float_is_zero(record.selling_price, precision_digits=2):
    #             if float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
    #                 raise exceptions.ValidationError("Selling price cannot be lower than 90 percent of the expected price!")

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if(tools.float_compare(record.expected_price,record.selling_price,precision_digits = 2) == 1):
                if(tools.float_compare(record.selling_price,(0.9*record.expected_price),precision_digits = 2) == -1):
                    raise exceptions.ValidationError("Selling price cannot be lower than 90'%' of the expected price.")

    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_cancelled(self):
        for record in self:
            if(record.state not in ['new','cancelled']):
                raise exceptions.UserError("Only new and cancelled properties can be deleted.")

    def offers_wizard(self):
        # for single record
        # self.ensure_one()

        return {
            'name': "Add Offer(s)",
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'wizard.add.offer',
            'target': 'new',
        }
           
    