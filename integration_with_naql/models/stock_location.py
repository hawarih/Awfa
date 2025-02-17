from odoo import api, fields, models


class StockLocation(models.Model):
    _inherit = 'stock.location'

    naql_id = fields.Char(string='Naql ID', copy=True, store=True)
