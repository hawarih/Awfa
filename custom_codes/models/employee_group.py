from odoo import api, fields, models


class EmployeeGroup(models.Model):
    _name = 'employee.group'
    _description = 'Employee Group'

    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Name must be unique'),
    ]