from odoo import api, fields, models


class StockArea(models.Model):
    _name = 'stock.area'
    _description = 'Stock Area'

    city_ids = fields.One2many(comodel_name='stock.city', inverse_name='area_id', string='City', store=True)
    name = fields.Char(string='Name', copy=True, required=True, store=True)
