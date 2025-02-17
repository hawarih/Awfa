from odoo import api, fields, models


class EmployeeSubgroup(models.Model):
    _name = 'employee.subgroup'
    _description = 'Employee Subgroup'

    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Name must be unique'),
    ]