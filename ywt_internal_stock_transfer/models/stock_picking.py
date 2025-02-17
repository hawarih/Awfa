from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    driver_in = fields.Many2one(comodel_name='vehicle.driver', string='Driver In', store=True)
    driver_out = fields.Many2one(comodel_name='vehicle.driver', string='Driver Out', store=True)
    has_no_important_group = fields.Boolean(string='Has No Important Group', readonly=True)
    internal_stock_transfer_id = fields.Many2one(comodel_name='ywt.internal.stock.transfer', string='Inter Stock Transfer', copy=True, store=True)
    stock_transfer_type = fields.Selection(string='Transfer Type', selection=[], related='internal_stock_transfer_id.transfer_type', readonly=True)
