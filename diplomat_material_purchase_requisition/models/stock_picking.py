from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    custom_requisition_id = fields.Many2one(comodel_name='material.purchase.requisition', string='Purchase Requisition', readonly=True, store=True)
