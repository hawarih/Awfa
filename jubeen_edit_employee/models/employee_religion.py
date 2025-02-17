from odoo import api, fields, models


class EmployeeReligion(models.Model):
    _name = 'employee.religion'
    _description = 'Employee Religion'

    name = fields.Char(string='Name', copy=True, store=True)
