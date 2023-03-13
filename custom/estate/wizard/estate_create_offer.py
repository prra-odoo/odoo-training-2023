from odoo import models,fields,Command,api
class EstateOffer(models.TransientModel):
    _name="estate.wizard"
    _description="estate wizard for property"


    name=fields.Many2one("res.partner")
    price=fields.Integer()
    # count=fields.Integer(default=0,readonly=True,compute="_compute_count")

    # @api.depends("")
    # def _compute_count(self):
    #     self.count=len(self.env.context.get('active_ids'))
        



    def action_add_offer(self):
        selected_ids = self.env.context.get('active_ids')
        breakpoint()
        selected_records = self.env['estate.property'].browse(selected_ids)
        for record in selected_records:
            record.write({
                'offer_ids':[
                Command.create({
                'price':self.price,
                'partner_id':self.name.id,
                })
                ]
            })
        # breakpoint()
        # for d in x:
            # breakpoint()
        # for record in self:
        #     # breakpoint()
        #     print(record.name)