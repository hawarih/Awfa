from odoo import api, fields, models, _

import re


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    current_fuel = fields.Selection(string='Current fuel', selection=[('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1')], copy=True, store=True)

    
    def view_rental_contracts(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rental Contract',
            'res_model': 'rental.contract',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'target': 'current',
        }
 
