# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyOfferWizard(models.TransientModel):
    _name = 'estate.property.offer.wizard'
    # _inherit = 'estate.property.offer'
    _description = 'Property offer wizard'

    name = fields.Char()
    # offer_ids = fields.Many2many('estate.property.offer', 'property_id', string="Offers")

    price = fields.Float('Price')
    status = fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    buyer_id = fields.Many2one('res.partner')

    # def create_offer(self):
    #     active_ids=self._context.get('active_ids')
    #     for record in active_ids:
    #         property_id=self.env['estate.property'].browse(record)
    #         property_id.write({
    #             "offer_ids":[
    #                 fields.Command.create({
    #                     "price" : self.price,
    #                     "partner_id" : self.partner_id.id,
    #                 })
    #             ]
    #         })
    #     return True

    def create_offer(self):
        active_ids = self._context.get('active_ids')
        for rec in active_ids:
            property_id = self.env['estate.property'].browse(rec)
            property_id.write({
                "offer_ids":[
                    fields.Command.create({
                        "price" : self.price,
                        "partner_id" : self.buyer_id.id,
                    })
                ]
            })

