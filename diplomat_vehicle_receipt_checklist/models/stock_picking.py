from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    has_checklist = fields.Boolean(string='Has Checklist', related='picking_type_id.has_checklist', readonly=True)
    is_vehicle_picking = fields.Boolean(string='Is Vehicle Picking', readonly=True)

