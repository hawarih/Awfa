from odoo import api, fields, models


class HrAttendancePolicy(models.Model):
    _name = 'hr.attendance.policy'
    _description = 'Hr Attendance Policy'

    absence_rule_id = fields.Many2one(comodel_name='hr.absence.rule', string='Absence Rule', copy=True, required=True, ondelete='restrict', store=True)
    diff_rule_id = fields.Many2one(comodel_name='hr.diff.rule', string='Difference Time Rule', copy=True, required=True, ondelete='restrict', store=True)
    late_rule_id = fields.Many2one(comodel_name='hr.late.rule', string='Late In Rule', copy=True, required=True, ondelete='restrict', store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    overtime_rule_ids = fields.Many2many(comodel_name='hr.overtime.rule', string='Overtime Rules', copy=True, relation='overtime_rule_policy_rel', column1='attendance_policy_col', column2='overtime_rule_col', store=True)
