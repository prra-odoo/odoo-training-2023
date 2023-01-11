from odoo import models,fields
from datetime import date

class CarRent(models.Model):
    _name="car.rent.info"
    _description="Car Information Model"

    name=fields.Char(string="Title",required=True)
    description=fields.Text('Description')
    postcode=fields.Char('Postcode')
    date_availabilty=fields.date('Date Availablity',copy=False,default=date.today())


