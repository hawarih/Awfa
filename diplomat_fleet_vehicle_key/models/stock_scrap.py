from odoo import api, fields, models


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    key_id = fields.Many2one(comodel_name='fleet.vehicle.key', string='Key', copy=True,  store=True)
