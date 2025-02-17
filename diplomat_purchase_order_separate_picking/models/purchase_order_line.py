from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    picked = fields.Integer(string='Picked', readonly=True, store=True)
    stock_picking_type_id = fields.Many2one(comodel_name='stock.picking.type', string='Deliver To', readonly=True, store=True)
