from odoo import fields, models ,api
from odoo.tools.date_utils import add
from odoo.exceptions import UserError
from odoo.tools import float_compare


class propertyoffer(models.Model):
    _name="estate.property.offer"
    _description = "property offer model"
    _order = "price desc"
    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "The price must be positive"),
    ]

    price = fields.Float("Price")
    partner_id = fields.Many2one("res.partner" ,required=True)
    property_id = fields.Many2one("estate.property",required=True)
    status = fields.Selection(selection= [('accepted','Accepted'),('refused','Refused')])
    validity = fields.Integer()
    date_deadline = fields.Date("Date Deadline", compute='_compute_date_deadline',inverse='_inverse_date_deadline')
    create_date = fields.Date(default=fields.Datetime.now(),readonly =True)
    property_type_id=fields.Many2one("estate.property.type", related = "property_id.property_type_id", store=True)

    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = add(record.create_date,days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - record.create_date).days

    def accept_action(self):
        for record in self:
            record.status='accepted'
            record.property_id.state='offer_accepted'
            # record.state='offer recieved'
        return True
    
    def refused_action(self):
        for record in self:
            record.status='refused'
            
            # record.state='offer accepted'