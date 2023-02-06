from odoo import fields,models,api,Command

class WizardPropertyOffer(models.Model):
    _name = "wizard.property.offer"
    _description = "Wizard for making an offer"
    
    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused'),], copy=False)
    property_ids = fields.Many2many("real.estate.property")
    # buyer_id = fields.Many2one(related='porperty_id.buyer_id')
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    
    
    def action_add_offer(self):
        print(self.read())
        print(self.price)
        print(self.status)
        print(self.buyer_id)
        print(self.property_ids)
        print("You successfully clicked on wizard......")
        
        vals = self.env['real.estate.property.offer'].browse(self._context.get('active_ids')).sudo().create(
            (0,0,[{
                'price':self.price,
                'status':self.status,
                'partner_id':self.buyer_id.id,
                'property_id':self.property_ids.id,
            }]),
        )
        return vals