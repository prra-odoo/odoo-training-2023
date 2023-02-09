from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name='estate.property.tag'
    _description='adding property tags in property'

    price=fields.Float(string='Price',
		help="this is for property offer price")
    status=fields.Selection(selection=[('accepted','Accepted'),('refused','Refused')],
		copy=False,
		string="status")
    partner_id=fields.Many2one('res.partner',
        string="Partner",
        required=True)
    property_id=fields.Many2one('estate.property',
        required=True,
        string="Property")
