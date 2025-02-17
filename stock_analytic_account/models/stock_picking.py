from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    show_analytic_distribution = fields.Boolean(string='Show Analytic Distribution', related='picking_type_id.show_analytic_distribution', readonly=True)
