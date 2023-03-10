from odoo import models, fields,api,Command

class WizardAddOffer(models.TransientModel):
    _name='wizard.add.offer'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
 
    price = fields.Float(string='Price')
    partner_id = fields.Many2one("res.partner", string="Partner", copy=False)

    def action_add(self):
        result = self.env['estate.property'].browse(self.env.context.get('active_ids'))
        for record in result:
            if (record.state in ['new','off_re'] and record.expected_price == 500000 and record.property_type_id.name == 'Residential'):
                record.write({
                    'offer_ids':[
                        Command.create({
                            'price':self.price,
                            'partner_id':self.partner_id.id
                        })  
                    ]
                })