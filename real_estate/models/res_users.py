from odoo import models,fields
class res_user(models.Model):
    
    _inherit='res.users'

    property_ids=fields.One2many('estate.property','sales_id')
    demo=fields.Integer()
    
# class newresuser(models.Model):
#      _name='new.res.user'
#      _inherit='estate.property.type'

#      demo2=fields.Integer(required=True)

# class propertyoffer(models.Model):
#       _name='property.offer'
#       _inherits = {'estate.property.offer': 'offer_ids'}

#       name=fields.Char(required=True)
#       offer_id=fields.Many2one('estate.property.offer')