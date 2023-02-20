from odoo import fields ,_, models, Command

class estateWizard(models.TransientModel):
    _name= "estate.wizard"
    _description = "Make payment invoice"
    
    price = fields.Integer(string='Price')   
    buyer_id = fields.Many2one("res.users",string="Partner id")
    salesman_id =fields.Many2one("res.partner", string="SalesMan")    
    def action_done(self):
        record = self.env['estate.property'].browse(self.env.context.get('active_ids'))   
        for rec in record:
            rec.write({
                'offer_ids' :[Command.create({
                    'price' :  self.price,
                    'partner_id' : self.salesman_id.id,
                    
                })]                
            })