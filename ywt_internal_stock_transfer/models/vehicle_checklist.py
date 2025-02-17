from odoo import api, fields, models


class VehicleChecklist(models.Model):
    _inherit = 'vehicle.checklist'

    internal_stock_transfer_id = fields.Many2one(comodel_name='ywt.internal.stock.transfer', string='Inter Stock Transfer', related='stock_move_id.picking_id.internal_stock_transfer_id', readonly=True)
    km_in = fields.Float(string='K.M IN', copy=True, store=True)
    km_out = fields.Float(string='K.M OUT', copy=True, store=True)
    vendor_km = fields.Float(string='Vendor K.M', copy=True, store=True)
