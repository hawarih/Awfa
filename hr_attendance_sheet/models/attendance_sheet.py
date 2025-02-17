from odoo import api, fields, models


class AttendanceSheet(models.Model):
    _name = 'attendance.sheet'
    _description = 'Attendance Sheet'

    att_policy_id = fields.Many2one(comodel_name='hr.attendance.policy', string='Attendance Policy ', copy=True, required=True, ondelete='restrict', store=True)
    att_sheet_line_ids = fields.One2many(comodel_name='attendance.sheet.line', inverse_name='att_sheet_id', string='Attendances', readonly=True, store=True)
    code = fields.Char(string='Code', related='employee_id.code', readonly=True, store=True)
    date_from = fields.Date(string='From', copy=True, required=True, store=True)
    date_to = fields.Date(string='To', copy=True, required=True, store=True)
    department_id = fields.Many2one(comodel_name='hr.department', string='Department', related='employee_id.department_id', readonly=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True, required=True, ondelete='restrict', store=True)
    name = fields.Char(string='name', copy=True, translate=True, store=True)
    no_absence = fields.Integer(string='No of Absence Days', readonly=True, store=True)
    no_difftime = fields.Integer(string='No of Diff Times', readonly=True, store=True)
    no_late = fields.Integer(string='No of Lates', readonly=True, store=True)
    no_overtime = fields.Integer(string='No of overtimes', readonly=True, store=True)
    no_unpaid_leave = fields.Integer(string='No of Un Paid Leaves', readonly=True, store=True)
    no_wd = fields.Float(string='No of worked days', readonly=True, store=True)
    no_weekend_holidays = fields.Float(string='No of weekends and Holidays', readonly=True, store=True)
    payslip_id = fields.Many2one(comodel_name='hr.payslip', string='PaySlip', store=True)
    state = fields.Selection(string='Status', help=""" * The 'Draft' status is used when a HR user is creating a new  attendance sheet. 
* The 'Confirmed' status is used when  attendance sheet is confirmed by HR user.
* The 'Approved' status is used when  attendance sheet is accepted by the HR Manager.""", selection=[('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Approved')], 
                                                                                        default='draft', required=True, readonly=True, index=True, store=True)
    tot_absence = fields.Float(string='Total absence Hours', readonly=True, store=True)
    tot_difftime = fields.Float(string='Total Diff time Hours', readonly=True, store=True)
    tot_late = fields.Float(string='Total Late In', readonly=True, store=True)
    tot_overtime = fields.Float(string='Total Over Time', readonly=True, store=True)
    tot_weekend_holidays = fields.Float(string='Total Weekends And Holidays', readonly=True, store=True)
    tot_wh = fields.Float(string='Total Working Hours', readonly=True, store=True)
    work_location_id = fields.Many2one(comodel_name='hr.work.location', string='Work Location', related='employee_id.work_location_id', readonly=True, store=True)

    def get_attendances(self):
        pass
    
    def calculate_att_data(self):
        pass
    
    def create_payslip(self):
        pass
    
    def action_attsheet_confirm(self):
        pass
    
    def action_attsheet_approve(self):
        pass
    
    def action_attsheet_draft(self):
        pass
    
    def create_payslip(self):
        pass