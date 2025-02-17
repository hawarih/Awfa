from odoo import api, fields, models


class ScrapKeyWiz(models.Model):
    _name = 'scrap.key.wiz'
    _description = 'Scrap Key Wiz'

    location_id = fields.Many2one(comodel_name='stock.location', string='Source Location', copy=True,  store=True)
    lot_id = fields.Many2one(comodel_name='stock.lot', string='Serial number', copy=True,  store=True)
    origin = fields.Char(string='Source Document', copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True,  store=True)
    product_uom_id = fields.Many2one(comodel_name='uom.uom', string='unit', copy=True,  store=True)
    scrap_location_id = fields.Many2one(comodel_name='stock.location', string='Scrap Location', copy=True,  store=True)
    scrap_qty = fields.Float(string='Scrap Qty', copy=True, readonly=True, store=True)

    def action_validate(self):
        pass