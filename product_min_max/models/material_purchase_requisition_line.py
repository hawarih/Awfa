from odoo import api, fields, models


class MaterialPurchaseRequisitionLine(models.Model):
    _inherit = 'material.purchase.requisition.line'

    purchase_id = fields.Many2one(comodel_name='purchase.type', string='Purchase Type', copy=True, required=True, ondelete='restrict', store=True)
    requisition_type = fields.Selection(string='Requisition Action', selection=[('purchase', 'Purchase Order')], copy=True, required=True, store=True)
