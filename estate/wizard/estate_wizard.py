from odoo import fields,models,Command

class EstateWizard(models.TransientModel):
    _name="estate.wizard"
    _description="Estate Offer Wizard"


    price=fields.Float(string="Price")
    partner_id=fields.Many2one('res.partner',string="Partner")
    status=fields.Selection(
        string="Status",
        selection=[
    ('accepted','Accepted'),('refused','Refused')
        ]
    )


    def make_offer(self):
        get_properties=self.env['estate.property'].browse(self.env.context.get('active_ids'))

        for record in get_properties:
         record.write({
            'offer_ids':[
            Command.create(
                {
                    'price':self.price,
                    'partner_id':self.partner_id.id
                }
            )
            ]

        }

        )        

