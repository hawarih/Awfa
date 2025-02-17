from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    inventory_id = fields.Many2one(comodel_name='stock.inventory', string='Inventory', copy=True, ondelete='set null', store=True)
