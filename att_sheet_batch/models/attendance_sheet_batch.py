from odoo import api, fields, models


class AttendanceSheetBatch(models.Model):
    _name = 'attendance.sheet.batch'
    _description = 'Attendance Sheet Batch'

    att_sheet_ids = fields.One2many(comodel_name='attendance.sheet', inverse_name='batch_id', string='Attendance Sheets', store=True)
    category_ids = fields.Many2many(comodel_name='hr.employee.category', string='Tags', copy=True, relation='employee_category_att_batch_rel', column1='batch_id', column2='category_id', store=True)
    date_from = fields.Date(string='From', copy=True, required=True, store=True)
    date_to = fields.Date(string='To', copy=True, required=True, store=True)
    department_ids = fields.Many2many(comodel_name='hr.department', string='Departments', copy=True, relation='attendance_sheet_batch_hr_department_rel', column1='attendance_sheet_batch_id', column2='hr_department_id', store=True)
    employee_ids = fields.Many2many(comodel_name='hr.employee', string='Employees', copy=True, relation='employee_shift_att_batch_rel', column1='batch_id', column2='employee_id', store=True)
    name = fields.Char(string='Name', copy=True, store=True)
    payslip_batch_id = fields.Many2one(comodel_name='hr.payslip.run', string='Payslip Batch', copy=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('att_gen', 'Attendance Sheets Generated'), 
                                                         ('att_sub', 'Attendance Sheets Submitted'), ('done', 'Close')], 
                                                        default='draft', required=True, readonly=True, index=True, store=True)
    struct_id = fields.Many2one(comodel_name='hr.payroll.structure', string='Structure', copy=True, store=True)


    def gen_att_sheet(self):
        pass
    
    def submit_att_sheet(self):
        pass
    
    def action_done(self):
        pass
    
    def return_payslips(self):
        pass


