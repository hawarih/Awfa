from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    maintenance_request_count = fields.Integer(string='Maintenance Request Count', readonly=True)
    vehicle_preventive_maintenance_count = fields.Integer(string='Vehicle Preventive Maintenance Count', readonly=True)

    def action_open_maintenance_request(self):
        pass

    def action_open_vehicle_preventive_maintenance(self):
        pass
