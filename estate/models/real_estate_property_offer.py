from odoo import models,fields,api

class EstatePropertyOfferModel(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate.property.offer'
    
    price = fields.Float(string="Price")
    status = fields.Selection(string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="status is used to show offer status",copy=False
    )
    partner_id = fields.Many2one('res.partner',required=True, index=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline
    
    def _inverse_date_deadline(self):
        for record in self:
            record.date_deadline