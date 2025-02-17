from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    key_number = fields.Integer(string='Number of Keys', readonly=True)

    def action_get_vehicle_key(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Keys',
            'res_model': 'fleet.vehicle.key',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'context': {'create': 0,},
            'target': 'current',
        }
