from odoo import api, fields, models


class EmployeeLine(models.Model):
    _name = 'employee.line'
    _description = 'Employee Line'

    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, store=True)
    note = fields.Char(string='Note', copy=True, store=True)
    phone = fields.Char(string='Phone', copy=True, store=True)
    relation_id = fields.Many2one(comodel_name='employee.emergency.contact', string='Relation', copy=True, store=True)
