from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    is_generalized = fields.Boolean(string='Is Generalized', copy=True, store=True)
    is_waiting_generalization = fields.Boolean(string='Is Waiting Generalization', copy=True, store=True)
