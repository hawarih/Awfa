from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    age = fields.Integer(string='Age', readonly=True)
    blood_group = fields.Selection(string='BLOOD GROUP', selection=[('a', 'A'), ('b', 'B'), ('ab', 'AB'), ('o', 'O')], copy=True, store=True)
    gosi_no = fields.Char(string='GOSI No.', copy=True, store=True)
    line_id = fields.One2many(comodel_name='employee.line', inverse_name='employee_id', string='Line', store=True)
    passport_expiration_date = fields.Date(string='Passport Expiration Date', copy=True, store=True)
    payment_method = fields.Selection(string='Payment Method', selection=[('bank_account', 'BANK ACCOUNT'), ('saire', 'SAIRE'), ('salary_card', 'SALARY CARD')], copy=True, store=True)
    place_of_issue = fields.Char(string='Place Of Issue', copy=True, store=True)
    religion_id = fields.Many2one(comodel_name='employee.religion', string='Religion', copy=True, store=True)
    rh_factory = fields.Selection(string='RH Factory', selection=[('+', '+'), ('-', '-')], copy=True, store=True)
