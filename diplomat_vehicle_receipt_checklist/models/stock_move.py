from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    can_check = fields.Boolean(string='Can Check', readonly=True)
    checklist_state = fields.Selection(string='Checklist State', selection=[('draft', 'Draft'), ('done', 'Done')], copy=True, readonly=True, store=True)
    vehicle_checklist_id = fields.Many2one(comodel_name='vehicle.checklist', string='Vehicle Checklist', copy=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', related='product_id.vehicle_id', readonly=True)

    def action_open_checklist(self):
        pass