from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_picking_created = fields.Boolean(string='Is Picking Created', readonly=True)
    separate_stock_picking = fields.Boolean(string='Separate Stock Picking', related='purchase_type_id.separate_stock_picking', readonly=True)
