from odoo import api, fields, models


class VehicleDriver(models.Model):
    _name = 'vehicle.driver'
    _description = 'Vehicle Driver'

    count_orders = fields.Integer(string='Count Orders', readonly=True)
    name = fields.Char(string='Name', copy=True, store=True)
    state = fields.Selection(string='State', selection=[('free', 'Free'), ('busy', 'Busy')], store=True, default='free')

    def action_view_stock_transfer(self):
        pass