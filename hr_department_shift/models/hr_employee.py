from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    hr_shifts = fields.Many2many(comodel_name='hr.department.shift.lines', string='Shifts', copy=True, relation='hr_department_shift_lines_hr_employee_rel', column1='hr_employee_id', column2='hr_department_shift_lines_id', store=True)
