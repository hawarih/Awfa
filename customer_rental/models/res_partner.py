from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    
    def show_rental_contracts(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rental Contract',
            'res_model': 'rental.contract',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'target': 'current',
        }