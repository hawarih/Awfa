from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    is_damaged = fields.Boolean(string='Is Damaged', copy=True, store=True)
