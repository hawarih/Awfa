from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    purchase_order_id = fields.Many2one(comodel_name='purchase.order', string='Purchase Order', copy=True, ondelete='set null', store=True)
    purchase_type_id = fields.Many2one(comodel_name='purchase.type', string='Purchase Order Type', related='purchase_order_id.purchase_type_id', readonly=True)
