from odoo import models, fields


class resUsers(models.Model):
    _inherit = "res.users"


    property_ids = fields.One2many('estate.property', 'salesman_id', string="Property", domain=[("state", "in", ["new","received"])] )
    demo1 = fields.Char()
    

# class estateCountry(models.Model):
#     _name="estate.country"
#     _inherits = {'res.country': 'country_id', 'res.country.state': 'state_id'}


#     country_id = fields.Many2one('res.country', string="country")
#     state_id = fields.Many2one('res.country.state', string='state')

#     demo = fields.Char()