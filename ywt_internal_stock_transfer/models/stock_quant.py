from odoo import api, fields, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    available_qty = fields.Float(string='Available Quantity', help="""On hand quantity which hasn't been reserved on a transfer, in the default unit of measure of the product""", related='available_quantity', readonly=True, store=True)
