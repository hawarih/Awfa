from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    call_center = fields.Boolean(string='Call Center', copy=True, store=True)
    call_center_days = fields.Integer(string='Call Center Days', copy=True, store=True)
    officer = fields.Boolean(string='Officer', copy=True, store=True)
    officer_days = fields.Integer(string='Officer Days', copy=True, store=True)
    rental_area_manager = fields.Boolean(string='Rental Area Manager', copy=True, store=True)
    rental_area_manager_days = fields.Integer(string='Rental Area Manager Days', copy=True, store=True)
