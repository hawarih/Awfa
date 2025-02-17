from odoo import api, fields, models


class SeparatePicking(models.TransientModel):
    _inherit = 'separate.picking'

    picking_type_ids = fields.Many2many(comodel_name='stock.picking.type', string='Picking Type', readonly=True)
