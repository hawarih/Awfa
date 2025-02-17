from odoo import api, fields, models


class GpsVehicleHistory(models.Model):
    _name = 'gps.vehicle.history'
    _description = 'Gps Vehicle History'

    date = fields.Date(string='Date', copy=True, store=True)
    gps_id = fields.Many2one(comodel_name='gps.gps', string='GPS', copy=True, store=True)
    state = fields.Selection(string='State', selection=[('assigned', 'Assigned'), ('unassigned', 'Unassigned')], store=True)
    user_id = fields.Many2one(comodel_name='res.users', string='User', copy=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, store=True)
