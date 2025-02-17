from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    def gps_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'GPS History',
            'res_model': 'gps.vehicle.history',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'target': 'current',
        }