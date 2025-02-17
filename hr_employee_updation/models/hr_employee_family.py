from odoo import api, fields, models


class HrEmployeeFamily(models.Model):
    _name = 'hr.employee.family'
    _description = 'Hr Employee Family'

    birth_date = fields.Date(string='DOB', copy=True, store=True, )
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', help="""Select corresponding Employee""", copy=True, ondelete='set null', store=True)
    member_contact = fields.Char(string='Contact No', copy=True, store=True)
    member_name = fields.Char(string='Name', copy=True, store=True)
    relation_id = fields.Many2one(comodel_name='hr.employee.relation', string='Relation', help="""Relationship with the employee""", copy=True, ondelete='set null', store=True)
