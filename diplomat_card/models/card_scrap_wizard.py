from odoo import api, fields, models


class CardScrapWizard(models.TransientModel):
    _name = 'card.scrap.wizard'
    _description = 'Card Scrap Wizard'

    location_id = fields.Many2one(comodel_name='stock.location', string='Source Location', copy=True, ondelete='set null', store=True)
    lot_id = fields.Many2one(comodel_name='stock.lot', string='Lot/Serial', copy=True, ondelete='set null', store=True)
    origin = fields.Char(string='Source Document', copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, ondelete='set null', store=True)
    scrap_location_id = fields.Many2one(comodel_name='stock.location', string='Scrap Location', copy=True, ondelete='set null', store=True)
    scrap_qty = fields.Float(string='Scrap Qty', copy=True, readonly=True, store=True)

    def button_confirm(self):
        pass
