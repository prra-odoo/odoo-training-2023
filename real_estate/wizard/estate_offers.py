from odoo import api, fields, models, Command, _


class estateApplyOffer(models.TransientModel):
    _name = 'estate.apply.offer.wizard'
    _description = 'Estate Apply Offer Wizard'
   
    price = fields.Float('Price')
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)

    def action_done(self):
        records = self.env['estate.property'].browse(self.env.context.get('active_ids'))
        for rec in records:
            rec.write({
                'offer_ids': [
                    Command.create({
                        'price': self.price,
                        'partner_id': self.partner_id.id
                })
                ]

            })