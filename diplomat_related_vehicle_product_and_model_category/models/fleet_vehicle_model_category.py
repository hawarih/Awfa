from odoo import api, fields, models


class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
