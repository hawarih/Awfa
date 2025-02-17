from odoo import api, fields, models


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    gps_id = fields.Many2one(comodel_name='gps.gps', string='Gps', copy=True, store=True)
