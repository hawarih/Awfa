from odoo import api, fields, models


class StockReportQuantityByLocation(models.TransientModel):
    _name = 'stock.report.quantity.by.location'
    _description = 'Stock Report Quantity By Location'

    default_code = fields.Char(string='Internal Reference', copy=True, store=True)
    location_id = fields.Many2one(comodel_name='stock.location', string='Location', copy=True, required=True, ondelete='cascade', store=True)
    product_category_id = fields.Many2one(comodel_name='product.category', string='Product Category', copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, required=True, ondelete='cascade', store=True)
    product_tmpl_id = fields.Many2one(comodel_name='product.template', string='Product Template', related='product_id.product_tmpl_id', readonly=True, store=True)
    quantity = fields.Float(string='Quantity', copy=True, store=True)
    uom_id = fields.Many2one(comodel_name='uom.uom', string='Product UoM', copy=True, store=True)
    wiz_id = fields.Many2one(comodel_name='stock.report.quantity.by.location.prepare', string='Wiz', copy=True, store=True)
