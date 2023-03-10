from odoo import models , fields,Command

class AddOfferWizard(models.TransientModel):
    _name="add.offer.wizard"
    _description="this is a wizard used for adding offer in the selected property"


    price=fields.Float(string="Offer Price", required=True)
    # offer_status=fields.Selection(
    #     selection=[('accepted','Accepted'),('refused','Refused')],
    #     string="Status"
    # )
    buyer_id=fields.Many2one("res.partner" , string="Buyer",copy=False)



    def add_offer_function(self):
        result = self.env['estate.property'].browse(self.env.context.get('active_ids'))
        for record in result:
            if (record.state in ['new','offer_received'] and record.expected_price == 500000 and record.property_type_id.name == 'Residential'):
                record.write({
                    'offer_ids':[
                        Command.create({
                            'price':self.price,
                            'partner_id':self.buyer_id.id
                        })
                    ]
                })
