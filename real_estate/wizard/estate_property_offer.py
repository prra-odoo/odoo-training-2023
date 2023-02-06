from odoo import fields,models,Command

class WizardPropertyOffer(models.Model):
    _name = "wizard.property.offer"
    _description = "Wizard for making an offer"
    
    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused'),], copy=False)
    property_ids = fields.Many2many("real.estate.property")
    # buyer_id = fields.Many2one(related='porperty_id.buyer_id')
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    
    
    def action_add_offer(self):
        
        active_ids = self._context.get('active_ids')
        if active_ids:
            for prop in active_ids:
                return self.env['real.estate.property'].browse(prop).write({
                    'offer_ids' : [
                        Command.create({
                        'price':self.price,
                        'status':self.status,
                        'partner_id':self.buyer_id.id,
                    }),]
                })
    
