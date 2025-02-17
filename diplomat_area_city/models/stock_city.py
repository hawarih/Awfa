from odoo import api, fields, models


class StockCity(models.Model):
    _name = 'stock.city'
    _description = 'Stock City'

    area_id = fields.Many2one(comodel_name='stock.area', string='Area', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, store=True)
