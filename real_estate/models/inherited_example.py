from odoo import fields,models,api

class Resusers(models.Model):
    _name="inherited.model.example"
    _inherit="estate.property.tag"
    _description = "It has no description"


    funny = fields.Char(required=True)

    