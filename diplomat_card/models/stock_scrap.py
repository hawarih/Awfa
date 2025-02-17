from odoo import api, fields, models


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    card_id = fields.Many2one(comodel_name='fleet.card', string='Card', copy=True, ondelete='set null', store=True)
