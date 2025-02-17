from odoo import api, fields, models


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    checkin_location_id = fields.Many2one(comodel_name='hr.work.location', string='Checkin Location', copy=True,  store=True)
    checkout_location_id = fields.Many2one(comodel_name='hr.work.location', string='Checkout Location', copy=True,  store=True)
