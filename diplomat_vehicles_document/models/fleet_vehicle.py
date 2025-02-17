from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    attachment_number = fields.Integer(string='Number of Attachments', readonly=True)

    def action_get_attachment_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Attachments',
            'res_model': 'ir.attachment',
            'view_mode': 'kanban,tree,form',  # Opens the tree view, allows switching to form view
            'target': 'current',
        }