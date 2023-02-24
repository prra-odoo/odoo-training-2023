from odoo import models,fields,api,exceptions

class AcomPropertyModel(models.Model):
    _name="acom.property.model"
    _description="Table to hold property information"
    _sql_constraints=[
        ('unique_prop_name','unique(name)','Property name should be unique')
        ]

    name = fields.Char(required=True)
    propImg = fields.Image(string="Brand Image", max_width=150, max_height=150)
    propAddress = fields.Char(required=True, string="Address")
    propLocation = fields.Char(required=True,string="Location")
    propPostcode = fields.Integer(required=True, string="Postcode")
    propOccupancy = fields.Integer(string="Occupied", readonly=True,compute="_compute_occupancy")
    totalOccupancy = fields.Integer(string="Total Occupancy",readonly=True,compute="_compute_total_occupancy")
    propRentalIncome = fields.Integer(string="Rental Income", readonly=True,compute="_compute_rental_income")
    propRoomsNumber = fields.Integer(string="No. of Rooms")
    propFloors = fields.Integer(string="No. of Floors")
    propFor = fields.Selection(string='For',
        selection=[('boys', 'Boys'), ('girls', 'Girls')],
        help="Boys/Girls Only")
    active = fields.Boolean(default = True, string="Active")
    propEachRoomSharing = fields.Integer()
    propRooms_ids = fields.One2many('acom.rooms.model','property_id')
    propTenatAllocation_ids = fields.One2many('acom.tenant.model','propAllocated_id')
    roomLen = fields.Integer()

    @api.depends("propRooms_ids")
    def _compute_occupancy(self):
        for record in self:
            record.propOccupancy = sum(record.propRooms_ids.mapped("currentCap"))
            record.roomLen = len(record.propRooms_ids)
            if(record.roomLen>record.propRoomsNumber):
                raise exceptions.UserError("Rooms cannot be more than %d" %record.propRoomsNumber)

    @api.depends("propRoomsNumber","propEachRoomSharing")
    def _compute_total_occupancy(self):
        for record in self:
            record.totalOccupancy = (record.propRoomsNumber*record.propEachRoomSharing)

    @api.depends("propRooms_ids.tenantRef_ids")
    def _compute_rental_income(self):
        for record in self:
            record.propRentalIncome = sum(record.propRooms_ids.tenantRef_ids.mapped("rent"))
