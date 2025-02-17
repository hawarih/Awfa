from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    can_change_state = fields.Boolean(string='Can Change State', readonly=True, default=True)
