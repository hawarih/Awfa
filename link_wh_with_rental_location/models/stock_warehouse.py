from odoo import api, fields, models


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    related_rental_location_id = fields.Many2one(comodel_name='stock.location', string='Related Rental Location', copy=True, store=True)
