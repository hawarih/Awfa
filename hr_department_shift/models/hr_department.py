from odoo import api, fields, models


class HrDepartment(models.Model):
    _inherit = 'hr.department'

    hr_shifts = fields.One2many(comodel_name='hr.department.shift.lines', inverse_name='hr_department_id', string='Shifts', required=True, store=True)
