from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo import exceptions

class AcomPropertyModel(models.Model):
    _name="acom.tenant.model"
    _description="Table to hold tenant information"

    name = fields.Char(required=True)
    tenantImg = fields.Image(string="Brand Image", max_width=150, max_height=150)
    contact = fields.Char(required=True)
    gender = fields.Selection(string="Gender",selection=[('male','Male'),('female','Female')])
    age = fields.Integer(readonly=True,compute="_compute_age")
    birthdate = fields.Date()
    dateOfJoining = fields.Date(required=True)
    rent=fields.Integer()
    color = fields.Integer()
    # nextDues = fields.Date()
    # nextDues = fields.Date(default = lambda self:(fields.Date.today()+relativedelta(month=+1)))
    propAllocated_id = fields.Many2one('acom.property.model')
    roomRef_id = fields.Many2one('acom.rooms.model', domain="[('property_id', '=', propAllocated_id)]")

    @api.depends("birthdate")
    def _compute_age(self):
        for record in self:
            record.age = relativedelta(fields.Date.today(),record.birthdate).years