from odoo import api,fields, models
from dateutil.relativedelta import relativedelta
class EstatePlan(models.Model):
    _name = "estate.property"
    _description = "estate property"
   

    name = fields.Char(required=True, string="Title")
    property_type_id = fields.Many2one("estate.property.types",string = "Property Types")
    property_tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")
    active = fields.Boolean(default = True)
    description = fields.Text()
    # state = fields.Text()
    postcode = fields.Char()
    dateavailability = fields.Date(copy=False, default=lambda self: fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    # living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    # garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = "Garden Orientaiton",
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        help = "Choose the direction",
        required=True
    )
    states = fields.Selection(
        string = "States",
        selection = [('new','New'),('offered received','Offered Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled'),],
        default='new',
        help = "Choose the state",
        required = True
    )
    buyer = fields.Many2one("res.partner", string="Buyer")
    salesperson = fields.Many2one("res.users",string = "Salesperson", default=lambda self: self.env.user)
    price = fields.Float(string="Price")
    status = fields.Selection(copy=False,selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id = fields.One2many("estate.property.offer","partner_id",required=True)
    property_id = fields.One2many("estate.property.offer","property_id",required=True)

    # class TotalAreaComputed(models.Model):
    #     _name = "totalarea.computed"

    totalarea = fields.Float(compute="_total_area")

    living_area = fields.Float()
    garden_area = fields.Float()
        
    @api.depends("living_area","garden_area")
    def _total_area(self):
        for area in self:
            area.totalarea = area.living_area + area.garden_area
