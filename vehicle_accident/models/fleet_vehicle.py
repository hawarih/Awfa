from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    is_ready_to_maintenance = fields.Boolean(string='Is Ready To Maintenance', copy=True, store=True)
