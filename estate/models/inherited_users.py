from odoo import models, fields

# classical inheritance
class inheritedModel(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many('estate.property' , 'salesperson_id' , string ="real estate property")




# Prototype inheritance
# class prototypeInheritance(models.Model):
#     _name = "aditya.estate.property"
#     _inherit = "estate.property"

#     demo_field = fields.Char()

# delegation inheritance

# class delegationInheritance(models.Model):
#     _name = "new.users"
#     _inherits = {'res.partner':'partner_id'}

#     partner_id = fields.Many2one('res.partner' )
#     vat = fields.Char(related = "partner_id.vat", inherited=True , string = "demo" ,store=True , required = True)
#     vat1 = fields.Char(related = "partner_id.vat", inherited=True , string = "demo" ,store=True , required = True)


  

  

