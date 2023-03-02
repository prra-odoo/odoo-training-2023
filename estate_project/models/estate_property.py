from odoo import models, Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def btn_sold(self):
        new_vals = {
            "name": self.name,
            "partner_id": self.buyer_id.id,
            "task_ids": [Command.create({
                "name": "Maintenance",
            })],
        }
        self.env["project.project"].create(new_vals)
        return super().btn_sold()
