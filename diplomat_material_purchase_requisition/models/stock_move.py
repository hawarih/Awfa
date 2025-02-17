from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    custom_requisition_line_id = fields.Many2one(comodel_name='material.purchase.requisition.line', string='Requisitions Line', store=True)
