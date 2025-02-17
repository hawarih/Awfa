from odoo import api, fields, models


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    custody_clearance = fields.Boolean(string='Custody Clearance', related='holiday_status_id.custody_clearance', readonly=True)
    holiday_name = fields.Char(string='Time Off Type', related='holiday_status_id.name', readonly=True, translate=True)
    hr_leave_id = fields.Many2one(comodel_name='hr.leave', string='Hr Leave', copy=True, store=True)
    relieving_request = fields.Boolean(string='Relieving Request', copy=True, store=True)
