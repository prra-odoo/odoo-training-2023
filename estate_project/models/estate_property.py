from odoo import models,Command

class EstateProject(models.Model):
    _inherit="real.estate.property"

    def action_state_sold(self):
        for record in self:
            self.env['real.estate.property'].check_access_rights("write")
            self.env['real.estate.property'].check_access_rule("write")
            self.check_access_rights("write")
            self.check_access_rule("write")
            pro=self.env['project.project'].sudo().search([('name','ilike','Cleaning')])
            if not pro:
                pro=self.env['project.project'].create({
                    'name':'Cleaning'
                })
            self.env['project.task'].sudo().create({
                'project_id':pro.id,
                'name':'Maintenance:'+record.name
            })
        return super().action_state_sold()