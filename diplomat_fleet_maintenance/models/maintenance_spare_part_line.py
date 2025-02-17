from odoo import api, fields, models


class MaintenanceSparePartLine(models.Model):
    _name = 'maintenance.spare.part.line'
    _description = 'Maintenance Spare Part Line'

    available_spare_parts = fields.Many2many(comodel_name='product.template', string='Available Spare Parts', readonly=True)
    demand = fields.Float(string='Demand', readonly=True)
    has_picking = fields.Boolean(string='Has Picking', readonly=True)
    maintenance_id = fields.Many2one(comodel_name='maintenance.request', string='Maintenance', copy=True,  store=True)
    picking_id = fields.Many2one(comodel_name='stock.picking', string='Picking', copy=True,  store=True)
    picking_state = fields.Selection(string='Status', help=""" * Draft: The transfer is not confirmed yet. Reservation doesn't apply.
 * Waiting another operation: This transfer is waiting for another operation before being ready.
 * Waiting: The transfer is waiting for the availability of some products.
(a) The shipping policy is "As soon as possible": no product could be reserved.
(b) The shipping policy is "When all products are ready": not all the products could be reserved.
 * Ready: The transfer is ready to be processed.
(a) The shipping policy is "As soon as possible": at least one product has been reserved.
(b) The shipping policy is "When all products are ready": all product have been reserved.
 * Done: The transfer has been processed.
 * Cancelled: The transfer has been cancelled.""", selection=[], related='picking_id.state', readonly=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True,  store=True)
    product_uom = fields.Many2one(comodel_name='uom.uom', string='Product Uom', copy=True,  store=True)
    product_uom_category_id = fields.Many2one(comodel_name='uom.category', string='Category', help="""Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios.""", related='product_id.uom_id.category_id', readonly=True)
    product_uom_qty = fields.Float(string='Product Uom Qty', copy=True, store=True)

