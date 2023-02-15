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
    garden_area = fields.Integer(compute="_compute_garden",readonly = False, store = True)
    active = fields.Boolean(default = True)
    state = fields.Selection(
        string="State",
        default="new",
        selection=[('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')]
    )
    
    garden_orientation = fields.Selection(
        string = "Type",
        selection = [('north','North'),('South','South'),('East','East'),('West','West'), ],
        help = "Choose the direction",
        compute = "_compute_garden",
        readonly = False,
        store = True
    )
    
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")
    buyer_id = fields.Many2one("res.partner",string="Buyer",copy=False)
    salesperson_id = fields.Many2one("res.users",string="Salesman",default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tags", string="Property Tags")
    offer_ids = fields.One2many("estate.property.offer","property_id", string="Offers")
    total_area = fields.Integer(compute="_compute_total")
    best_offer = fields.Float(compute = "_compute_bestoffer")
    
    #compute for total_area
    
    @api.depends("living_area","garden_area") #decorator
    
    def _compute_total(self):
        for record in self: 
            record.total_area = record.living_area + record.garden_area
    
    #compute for best_offer
            
    @api.depends("offer_ids.price")
    
    def _compute_bestoffer(self):
        for record in self:
            if record.offer_ids.mapped("price"):
                record.best_offer = max(record.offer_ids.mapped("price"))
            else:
                record.best_offer = 0
    
    #compute for garden_orientation and garden_area
    
    @api.depends("garden")
    
    def _compute_garden(self):
        for record in self:
                record.garden_orientation = "north" if record.garden == True else ""
                record.garden_area = 10 if record.garden == True else ""
                