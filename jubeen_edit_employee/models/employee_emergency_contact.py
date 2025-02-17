from odoo import api, fields, models


class EmployeeEmergencyContact(models.Model):
    _name = 'employee.emergency.contact'
    _description = 'Employee Emergency Contact'

    name = fields.Char(string='relation', copy=True, store=True)
