from odoo import fields, models


# Class Inheritance - In which we are inheriting parent model but there will be no model will be created
# Fields added in child model will be added to the parent model

# class InheritedModel(models.Model):
#     _inherit = "estate.property"

#     gym = fields.Boolean()

# Prototype Inheritance - In this we are inheriting from parent model along with that child model will also 
# be created - Fields added into this will only be added to child model

# class InheritedModel(models.Model):
#     _name = "inherited.model"
#     _inherit = "estate.property"

#     abc = fields.Boolean()
#     swimming_pool = fields.Boolean()

class EstatePropertyInheritedModel(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many("estate.property", "seller_id", domain="[('state', '=', 'new')]")