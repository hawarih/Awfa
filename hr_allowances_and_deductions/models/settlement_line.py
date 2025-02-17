from odoo import api, fields, models


class SettlementLine(models.Model):
    _name = 'settlement.line'
    _description = 'Settlement Line'

    allowance_deduction_id = fields.Many2one(comodel_name='allowance.deduction', string='Allowance Deduction', copy=True, store=True)
    amount = fields.Float(string='Amount', copy=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', related='allowance_deduction_id.employee_id', readonly=True)
    payslip_id = fields.Many2one(comodel_name='hr.payslip', string='Payslip', copy=True, store=True)
    state = fields.Selection(string='State', selection=[('not paid', 'Not Paid'), ('paid', 'Paid')], store=True)
