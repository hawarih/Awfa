from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    maintenance_id = fields.Many2one(comodel_name='maintenance.request', string='Maintenance', copy=True,  store=True)
