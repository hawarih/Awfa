from odoo import api, fields, models


class MaterialPurchaseRequisitionLine(models.Model):
    _name = 'material.purchase.requisition.line'
    _description = 'Material Purchase Requisition Line'

    description = fields.Char(string='Description', copy=True, required=True, store=True)
    partner_id = fields.Many2many(comodel_name='res.partner', string='Vendors', copy=True, relation='material_purchase_requisition_line_res_partner_rel', column1='material_purchase_requisition_line_id', column2='res_partner_id', store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, required=True, ondelete='restrict', store=True)
    product_uom_category_id = fields.Many2one(comodel_name='uom.category', string='Category', help="""Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios.""", related='product_id.uom_id.category_id', readonly=True)
    qty = fields.Float(string='Quantity', copy=True, required=True, store=True)
    requisition_id = fields.Many2one(comodel_name='material.purchase.requisition', string='Requisitions', copy=True, store=True)
    requisition_type = fields.Selection(string='Requisition Action', selection=[('purchase', 'Purchase Order')], copy=True, required=True, store=True)
    uom = fields.Many2one(comodel_name='uom.uom', string='Unit of Measure', copy=True, required=True, ondelete='restrict', store=True)
