from odoo import models,fields

class estate_Property_tag(models.Model):
      _name = "estate.property.tag"
      _description = "Real estate based advertisedment module for the property tag"
      _order="name"

      _sql_constraints =[                                                                                      
    
        ('name', 'unique(name)', "A tag name must be unique...!"),
      ]

      name = fields.Char(required=True)
      color=fields.Integer('color')