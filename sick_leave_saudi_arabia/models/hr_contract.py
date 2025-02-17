from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    hr_sick_leave_line_ids = fields.One2many(comodel_name='hr.sick.leave.line', inverse_name='hr_sick_leave_id', string='Hr Sick Leave Line', store=True)
