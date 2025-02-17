from odoo import api, fields, models


class GpsScrapWizard(models.TransientModel):
    _name = 'gps.scrap.wizard'
    _description = 'Gps Scrap Wizard'

    location_id = fields.Many2one(comodel_name='stock.location', string='Source Location', copy=True, store=True)
    lot_id = fields.Many2one(comodel_name='stock.lot', string='Lot/Serial', copy=True, store=True)
    origin = fields.Char(string='Source Document', copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, store=True)
    scrap_location_id = fields.Many2one(comodel_name='stock.location', string='Scrap Location', copy=True, store=True)
    scrap_qty = fields.Float(string='Scrap Qty', copy=True, readonly=True, store=True)

    def button_confirm(self):
        pass
