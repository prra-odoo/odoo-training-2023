from odoo import models,fields

class estate_property(models.Model):
    _name = "estate.property"
    _description = "It's a estate prooperty module"


    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='type',
        selection=[('lead','Lead'),('opportunity','Opportunity')],
        help="Type is used to separate Leads and Opportunities"
        )