from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    picking_type_ids = fields.Many2many(comodel_name='stock.picking.type', string='Picking Type', readonly=True)
