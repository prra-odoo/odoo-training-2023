from odoo import models ,fields,Command

class putpropertyOffers(models.TransientModel):
    _name = "estate.property.put.offer"
    _description = "this is wizard used to offer in multiple records"

    price = fields.Float()
    status = fields.Selection( selection = [("accepted","Accepted"),("refused","Refused")],copy = False)
    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('estate.property')
    property_type_id=fields.Many2one('estate.property.type')
    validity = fields.Integer(default= 7)
    create_date = fields.Date(default=fields.Datetime.now())

    def action_put_offer(self):
         properties=self.env['estate.property'].browse(self.env.context.get('active_ids'))
         for rec in properties:
             rec.write(
                {
                     'offer_ids': [Command.create(
                        {
                            'price':self.price,
                            'partner_id':self.partner_id.id,
                        }
                     )]
                    
                }
             )
         breakpoint()

            
       
        
            
        
        # store={
        #     'price':self.price,
        #     'partner_id':self.partner_id,
        #     'property_type_id':self.property_type_id,
        #     'validity':self.validity
        # }

        # properties = self.env['estate.property'].search([])
        # for record in properties.search([]):
        #     if properties.property_type_id == store['property_type_id']:
        #        print("_____________________________________")
        #        self.env['estate.property'].create(
        #         {
        #             'offer_ids':[
        #                 Command.create({
        #             'record.price': self.price,
        #             'record.partner_id':self.partner_id,

        #             })
        #         ]
                

        #         }
                
        #        )

          

          
                
