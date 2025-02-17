from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    att_policy_id = fields.Many2one(comodel_name='hr.attendance.policy', string='Attendance Policy', copy=True, store=True)
    gross = fields.Monetary(string='Gross', readonly=True)
    struct_id = fields.Many2one(comodel_name='hr.payroll.structure', string='Structure', copy=True, required=True, ondelete='restrict', store=True)
