from odoo import api, fields, models


class HrPolicyOvertimeLine(models.Model):
    _name = 'hr.policy.overtime.line'
    _description = 'Hr Policy Overtime Line'

    active_after = fields.Float(string='Apply after', help="""After this time the overtime will be calculated""", copy=True, store=True)
    attendance_policy_id = fields.Many2one(comodel_name='hr.attendance.policy', string='Attendance Policy', copy=True, store=True)
    overtime_rule_id = fields.Many2one(comodel_name='hr.overtime.rule', string='Name', copy=True, required=True, ondelete='restrict', store=True)
    rate = fields.Float(string='Rate', copy=True, store=True)
    type = fields.Selection(string='Type', selection=[('weekend', 'Week End'), ('workday', 'Working Day'), ('ph', 'Public Holiday')], copy=True, store=True)
