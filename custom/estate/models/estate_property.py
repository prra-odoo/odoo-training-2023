
from odoo import api,models,fields  
from dateutil.relativedelta import relativedelta
class EstateProperty(models.Model):
    _name="estate.property"
    _description="estate property project"
    name=fields.Char(required=True)
    active=fields.Boolean(default=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(default=lambda self:fields.Date.today()+relativedelta(months=3),copy=False)
    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer(default=0)
    garden_orientation=fields.Selection(
        string='Type',
        selection=[('N','North'),('S','South'),('E','East'),('W','West')],
        help="Choose direction"
    )   
    state=fields.Selection(
        string='State',
        selection=[('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        default='new',
        required=True
    )
    property_type_id=fields.Many2one("estate.property.types",string="Property Type")
    buyer=fields.Many2one("res.partner",copy=False)
    salesperson=fields.Many2one('res.users',default=lambda self: self.env.user)
    tag_ids=fields.Many2many('estate.property.tag')
    offer_id=fields.One2many('estate.property.offer','property_id')
    total_area=fields.Integer(compute="_compute_area")
    best_offer=fields.Float(compute="_compute_bestoffer",readonly=True)

    @api.depends("living_area","garden_area")
    def _compute_area(self):
        for record in self:
            self.total_area=self.living_area+self.garden_area

    @api.depends("offer_id.price")
    def _compute_bestoffer(self):
        for record in self:
            if record.offer_id:
                record.best_offer=max(record.offer_id.mapped('price'))
            else:
                record.best_offer=0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area=10
            self.garden_orientation='N'
        else:
            self.garden_area=0
            self.garden_orientation=''
        