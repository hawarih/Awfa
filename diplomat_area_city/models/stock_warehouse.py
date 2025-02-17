from odoo import api, fields, models


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    area_id = fields.Many2one(comodel_name='stock.area', string='Area', related='city_id.area_id', readonly=True, store=True)
    city_id = fields.Many2one(comodel_name='stock.city', string='City', copy=True,  store=True)
