from odoo import api, fields, models


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    custody_clearance = fields.Boolean(string='Custody Clearance', copy=True, store=True)
    maximum_days_number_request = fields.Integer(string='Maximum Days Number Request', copy=True, store=True)
