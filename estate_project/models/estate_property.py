from odoo import api, models,fields,Command

class EstateProperty(models.Model):
   
    _inherit = "estate.property"
    
    def action_sold(self):
        
        self.env['project.project'].create(
            {
                'name':'House Renovation',
                'task_ids' : [
                    
                    Command.create(
                        {
                            'name' : 'House Cleaning',
                        }
                    )
                ]
            }  
        )
        return super().action_sold()
    

    # to make link the between module create a bridge module
    
    # in bridge module we need the inherit the action from where we want to move to other Module
    
    # now to create the functionality of the other module we need to know the required fields
    # needed so we will use .create method and will pass the dic in tuple 
    
    # self.env [] is used to access the module
    
    
    # now to create the task for project module we can do it through adding the one2Many field
    # then using command .create we can create the task 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def action_sold(self):
    #     for rec in self :
    #         self.env['account.move'].create(
    #             {
    #                 'partner_id' : rec.buyer_id.id,
    #                 'move_type' :  'out_invoice',
                    
    #                 'invoice_line_ids' :[
                        
    #                  Command.create (
    #                                     {
    #                                     'name':'house available',
    #                                     'quantity':1,
    #                                     'price_unit':0.06*rec.selling_price,
    #                                     },
    #                             ),
    #                 Command.create (
    #                                     {
    #                                     'name':'admintrative fees',
    #                                     'quantity':1,
    #                                     'price_unit':100,
    #                                     },
    #                             ),
        
    #                             ],

    #             }   
               
    #         )
    #     return super().action_sold()
        
    
    