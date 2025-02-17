from odoo import api, fields, models


class HrSickLeaveLine(models.Model):
    _name = 'hr.sick.leave.line'
    _description = 'Hr Sick Leave Line'

    date_from = fields.Date(string='Date From', copy=True, store=True)
    date_to = fields.Date(string='Date To', copy=True, store=True)
    hr_sick_leave_id = fields.Many2one(comodel_name='hr.contract', string='Hr Sick Leave', copy=True, store=True)
    leave_id = fields.Many2one(comodel_name='hr.leave', string='Leave', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, store=True)
    number_of_days = fields.Float(string='Duration', copy=True, store=True)
    payslip_state = fields.Selection(string='Payslip Status', selection=[('paid', 'Paid'), ('not_paid', 'Not Paid')], readonly=True)
    time_off_state = fields.Selection(string='Time Off Status', selection=[('draft', 'To Submit'), ('confirm', 'To Approve'), ('refuse', 'Refused'), ('validate', 'Approved'), ('validate1', 'Second Approved')], copy=True, store=True)

    def open_sick_leave(self):
        pass