from odoo import api, fields, models


class MaintenanceTeam(models.Model):
    _inherit = 'maintenance.team'

    picking_type_id = fields.Many2one(comodel_name='stock.picking.type', string='Picking Type', copy=True,  store=True)
