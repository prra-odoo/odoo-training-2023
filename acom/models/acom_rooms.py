from odoo import models, fields,api,exceptions

class AcomRoomsModel(models.Model):
    _name = "acom.rooms.model"
    _description = "Each Room Model"
    _rec_name="roomNumber"
    # _sql_constraints=[
    #     (
    #     'unique_room_number',
    #     'UNIQUE (roomNumber)',
    #     'Room number should be unique'
    #     )
    #     ]

    roomNumber = fields.Integer()
    currentCap = fields.Integer(readonly=True,compute="_compute_current_cap")
    maxCap = fields.Integer(readonly=True,compute="_compute_max_cap")
    perHeadRent = fields.Integer(default=3500)
    tenantRef_ids = fields.One2many('acom.tenant.model','roomRef_id')
    property_id = fields.Many2one('acom.property.model')
    tenantLen = fields.Integer()

    @api.depends("tenantRef_ids")
    def _compute_current_cap(self):
        for record in self:
            record.currentCap = len(record.tenantRef_ids)
            record.tenantLen = len(record.tenantRef_ids)
            if(record.tenantLen>record.maxCap):
                raise exceptions.UserError("Maximum tenants per room can only be %d" %record.maxCap)

    @api.depends("property_id.propEachRoomSharing")
    def _compute_max_cap(self):
        for record in self:
            record.maxCap = record.property_id.propEachRoomSharing

    @api.constrains('roomNumber')
    def _unique_roomNumber(self):
        for record in self:
            if(record.roomNumber in self):
                raise exceptions.UserError("Room number should be unique")
