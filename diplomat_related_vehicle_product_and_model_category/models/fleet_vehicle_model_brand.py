from odoo import api, fields, models


class FleetVehicleModelBrand(models.Model):
    _inherit = 'fleet.vehicle.model.brand'

    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
