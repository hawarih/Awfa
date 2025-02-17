from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    custom_requisition_line_id = fields.Many2one(comodel_name='material.purchase.requisition.line', string='Requisitions Line', store=True)
