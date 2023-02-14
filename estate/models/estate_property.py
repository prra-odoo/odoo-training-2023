from odoo import api, models,fields
from odoo.tools.rendering_tools import relativedelta_proxy

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description='Real Estate Property'
    
    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date(copy = False,default = lambda self : fields.Date.today()+relativedelta_proxy(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy= False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default = True)
    state = fields.Selection(
        string="State",
        default="new",
        selection=[('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')]
    )
    garden_orientation = fields.Selection(
        string = "Type",
        selection = [('north','North'),('South','South'),('East','East'),('West','West'), ],
        help = "Choose the direction"
    )
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")
    buyer_id = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesperson_id = fields.Many2one("res.users",string="Salesman",default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tags", string="Property Tags")
    offer_ids = fields.One2many("estate.property.offer","property_id", string="Offers")
    total_area = fields.Integer(compute="_compute_total")
    best_offer = fields.Float(compute = "_best_offer")
    
    @api.depends("living_area","garden_area")
    
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
            
    @api.depends("offer_ids.price")
    
    def _best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped("price")) 