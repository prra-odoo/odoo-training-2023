from odoo import models, fields, api

class EstateType(models.Model):
    _name = "estate.property.type"
    _description = "This model will describe about type of houses"

    # ordering the list view by name 
    _order = "name"

    # creating a name field that will be stored in db
    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many('estate.property', "property_type_id")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")



    # defining sql constraints so that user cannot set same name again
    _sql_constraints = [
        (
            'check_unique_type_name',
            'unique (name)',
            'Name of the property type should be unique!'
        )
    ]

    @api.depends("offer_ids", "offer_count")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len
            (record.offer_ids)
