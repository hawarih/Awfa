from odoo import api, fields, models


class YwtInternalStockTransferLine(models.Model):
    _name = 'ywt.internal.stock.transfer.line'
    _description = 'Ywt Internal Stock Transfer Line'

    allowed_time = fields.Float(string='Allowed Time', readonly=True)
    available_quantity = fields.Float(string='Available Qty', readonly=True)
    consumed_time = fields.Float(string='Consumed Time', readonly=True)
    date_in = fields.Datetime(string='Date In', copy=True, store=True)
    date_out = fields.Datetime(string='Date Out', copy=True, store=True)
    deviation_state = fields.Selection(string='Status', selection=[('positive', 'Positive'), ('negative', 'Negative')], readonly=True)
    diff = fields.Float(string='Differance', readonly=True)
    driver_in = fields.Many2one(comodel_name='vehicle.driver', string='Driver In', readonly=True)
    driver_out = fields.Many2one(comodel_name='vehicle.driver', string='Driver Out', readonly=True)
    internal_stock_transfer_id = fields.Many2one(comodel_name='ywt.internal.stock.transfer', string='Internal Stock Transfer', required=True, ondelete='cascade', store=True)
    km_in = fields.Float(string='k.m in', readonly=True)
    km_limit = fields.Float(string='k.m limit', readonly=True)
    km_out = fields.Float(string='k.m out', readonly=True, store=True)
    new_product_ids = fields.Many2many(comodel_name='product.product', string='Product', related='internal_stock_transfer_id.product_ids', readonly=True)
    odometer = fields.Float(string='Last Odometer', help="""Odometer measure of the vehicle at the moment of this log""", related='product_id.vehicle_id.odometer', readonly=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', required=True, ondelete='cascade', store=True)
    product_ids = fields.Many2many(comodel_name='product.product', string='Product', readonly=True)
    qty = fields.Float(string='Quantity', required=True, store=True)
    quantity_on_hand = fields.Float(string='Qty On Hand', help="""Current quantity of products.
In a context with a single Stock Location, this includes goods stored at this Location, or any of its children.
In a context with a single Warehouse, this includes goods stored in the Stock Location of this Warehouse, or any of its children.
stored in the Stock Location of the Warehouse of this Shop, or any of its children.
Otherwise, this includes goods stored in any Stock Location with 'internal' type.""", related='product_id.qty_available', readonly=True)
    second_product_ids = fields.Many2many(comodel_name='product.product', string='Second Product', related='internal_stock_transfer_id.second_product_ids', readonly=True)
    traveled_distance = fields.Float(string='Traveled Distance', readonly=True)
