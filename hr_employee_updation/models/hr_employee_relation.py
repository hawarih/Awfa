from odoo import api, fields, models


class HrEmployeeRelation(models.Model):
    _name = 'hr.employee.relation'
    _description = 'Hr Employee Relation'

    name = fields.Char(string='Relationship', help="""Relationship with thw employee""", copy=True, store=True)
