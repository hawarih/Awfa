from odoo import api, fields, models


class HrDepartmentShiftLines(models.Model):
    _name = 'hr.department.shift.lines'
    _description = 'Hr Department Shift Lines'

    end_date = fields.Date(string='End Date', copy=True, required=True, store=True)
    end_date_hijri = fields.Char(string='End Hijri Date', readonly=True)
    hr_department_id = fields.Many2one(comodel_name='hr.department', string='Department', copy=True,  store=True)
    hr_employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True,  store=True)
    start_date = fields.Date(string='Start Date', copy=True, required=True, store=True)
    start_date_hijri = fields.Char(string='Start Hijri Date', readonly=True)
    work_schedule = fields.Many2one(comodel_name='resource.calendar', string='Work Schedule', copy=True,  store=True)
