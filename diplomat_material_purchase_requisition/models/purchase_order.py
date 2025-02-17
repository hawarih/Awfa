from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    custom_requisition_id = fields.Many2one(comodel_name='material.purchase.requisition', string='Requisitions', store=True)
