from odoo import models

class estateAccountInvoice(models.Model):
    _inherit = "estate.property"

    def sold_product(self):
        print('print')
        return super(estateAccountInvoice,self).sold_product()
    def validity(self):
        print("validity")
        return super(estateAccountInvoice,self).sold_product()