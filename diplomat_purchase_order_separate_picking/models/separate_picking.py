from odoo import api, fields, models


class SeparatePicking(models.TransientModel):
    _name = 'separate.picking'
    _description = 'Separate Picking'

    purchase_order_id = fields.Many2one(comodel_name='purchase.order', string='Purchase Order', copy=True, store=True)
    separate_picking_line_ids = fields.One2many(comodel_name='separate.picking.line', inverse_name='separate_picking_id', string='Separate Picking Line', store=True)

    def action_confirm(self):
        pass
