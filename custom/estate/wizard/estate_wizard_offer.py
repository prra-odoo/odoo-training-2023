from odoo import api,fields, models,Command

class EstateWizardOffer(models.TransientModel):
    _name = "estate.wizard.offer"
    _description = "create offers wizard"

    price = fields.Float()
    partner_id = fields.Many2one('res.partner')
    count = fields.Integer(string="Property Count", compute='_compute_count')
    property_ids = fields.Many2many('estate.property', default=lambda self: self.env.context.get('active_ids'))
    
    @api.depends('property_ids')
    def _compute_count(self):
        for record in self:
            record.count = len(record.property_ids)
            print(record.property_ids)
    
    def action_create_offer(self):
        for record in self.property_ids:
            record.offer_ids = [Command.create({'partner_id':self.partner_id.id,'price':self.price})]