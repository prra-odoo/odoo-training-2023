from odoo import fields,models

class Users(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many("estate.property","salesmans_id",
                                    string = "Properties", 
                                    domain = "[('state','in',('new','received'))]",
                                    required=True,
                                    ondelete='cascade',
                                    store=True
                                    )
