from odoo import models, fields, Command


class EstateProperty(models.Model):
    # _name = "estate.property"
    # _description = "estate property Model"
    _inherit = 'estate.property'

    def action_sold(self):
        project = self.env['project.project'].create([{
            'name' : self.name,
            'type_ids' :[ Command.create({
            'name' : "New"
            
            })]
        }])
       
        self.env['project.task'].create([{
            'name' : "Maintainance",
            'project_id' : project.id,
            'partner_id' : self.partner_id.id,
        }])
        # self.env['project.task'].create([{
        #     # 'project_id': ,
        #     'invoice_date': fields.Date.today(),
        #     'line_ids': [
        #         Command.create({
        #             'name': self.name,
        #             'price_unit': self.selling_price * 0.06,
        #             'tax_ids' : False,
        #             'quantity': 1,

        #         }), Command.create({
        #             'name': "Administrative fees",
        #             'price_unit': 100,
        #             'tax_ids' : False,
        #             'quantity': 1,
        #         })]

        # }])
        return super().action_sold()
