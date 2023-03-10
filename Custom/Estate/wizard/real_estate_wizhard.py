from odoo import fields,models,Command

class RealEstateWizard(models.TransientModel):
    _name="real.estate.wizard"
    _description="creating a user interface for more relaibility"

    price = fields.Integer()
    # status = fields.Char()
    partner_id = fields.Many2one('res.partner')

    def calculate_property(self):
        sel_properties = self.env['estate.property'].browse(self.env.context.get('active_ids'))
        for record in sel_properties:
            if(record.state in ['new','offer_recieved'] and record.expected_price <= 500000 and record.property_type_id.name == 'Home'):
                record.write({
                    'offer_ids':[
                    Command.create({
                        'price':self.offer_amount,
                        'buyer_id':self.buyer_id.id
                        })
                    ]
                    })
                return {'type': 'ir.actions.act_window_close'}
        


























# breakpoint()
        # selected_property_ids = self.env.context.get('active_ids')
        # for i in selected_property_ids:
        #     if(i.state in ['new','offer_recieved'] and i.expected_price <= 500000 and i.property_type_ID.name == 'House'):
        #         self.env['estate.property.offer'].create(
        #             {
        #             'price':self.price,
        #             'partner_id' : self.partner_id.id,
        #             'property_id': i,
        #             }
        #         )
        #     return True