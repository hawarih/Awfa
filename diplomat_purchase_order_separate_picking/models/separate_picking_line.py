from odoo import api, fields, models


class SeparatePickingLine(models.TransientModel):
    _name = 'separate.picking.line'
    _description = 'Separate Picking Line'

    purchase_line_ids = fields.Many2many(comodel_name='purchase.order.line', string='Purchase Line', readonly=True)
    purchase_order_line_id = fields.Many2one(comodel_name='purchase.order.line', string='Products', copy=True, store=True)
    separate_picking_id = fields.Many2one(comodel_name='separate.picking', string='Separate Picking', copy=True, store=True)
    stock_picking_type_id = fields.Many2one(comodel_name='stock.picking.type', string='Deliver To', copy=True, store=True)
