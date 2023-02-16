from odoo import models,fields,api,exceptions
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last seen",default = lambda self : fields.Datetime().now())
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date("Available from",default = lambda self : fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float()
    selling_price = fields.Float(compute = "_compute_selling_price")
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(compute="_compute_garden",readonly=False)
    garden_orientation = fields.Selection(selection=[("north","North"),("south","South"),("east","East"),("west","West")],compute="_compute_garden",readonly=False)
    active = fields.Boolean(default = False)
    status = fields.Selection(selection=[("new","New"),("offer received","Offer Received"),("offer accepted","Offer Accepted"),("sold","Sold"),("canceled","Canceled")],default = "New",copy = False)
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")
    sales_person_id = fields.Many2one('res.users', string="Salesman",default = lambda self : self.env.user)
    buyer_id = fields.Many2one('res.partner', string="Buyer",compute="_compute_buyer_id")
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer','property_id')
    total_area = fields.Float(compute = "_compute_area")
    best_price = fields.Float(compute = "_compute_bestprice",default=0)

    @api.depends("living_area","garden_area")
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    @api.depends("offer_ids.price")

    def _compute_bestprice(self):
        for record in self:      
            if len(record.mapped('offer_ids.price')) > 0:
                record.best_price = max(record.mapped('offer_ids.price'))
            else:
                record.best_price = 0

    @api.depends("garden")

    def _compute_garden(self):
        for record in self:
            if(record.garden is True):
                record.garden_area = 10
                record.garden_orientation = "north"
            else:
                record.garden_area = 0
                record.garden_orientation = ""
    def action_sold(self):
        for record in self:
            if (record.status == "canceled"):
                raise exceptions.UserError("Canceled properties can't be sold!")
            else:
                record.status = "sold"
            
    def action_cancel(self):
        for record in self:
            record.status = "canceled"
    @api.depends("offer_ids.status")

    def _compute_selling_price(self):
        for record in self:
            flag = 0
            for field in record.offer_ids:
                if (field.status == "accepted"):
                    record.selling_price = field.price
                    flag = 1
            if(flag == 0):
                record.selling_price = 0
    def _compute_buyer_id(self):
        for record in self:
            flag = 0
            for field in record.offer_ids:
                if (field.status == "accepted"):
                    record.buyer_id = field.partner_id
                    flag = 1
            if(flag == 0):
                record.buyer_id = ""