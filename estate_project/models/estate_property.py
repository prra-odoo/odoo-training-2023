from odoo import models, Command


class EstateAccount(models.Model):
    _inherit = 'estate.property'

    def action_sold_button_header(self):
        for rec in self:
            id = self.env['project.project'].search(
                [('name', '=', 'Estate Project')]).id
            if not id:
                id = self.env['project.project'].create({
                    'name': "Estate Project",
                    'partner_id': rec.buyer_id.id,
                    'user_id': rec.salesperson_id.id,
                    'allow_timesheets': True
                }).id

            self.env['project.task'].create({
                'name': rec.name,
                'project_id': id,
                'tag_ids': [Command.create({
                    'name': rec.tag_ids.name,
                })],
            })
        return super(EstateAccount, self).action_sold_button_header()
