from odoo import api, fields, models


class RegisterNumber(models.Model):
    _name = 'register.number'
    _description = 'Register Number'

    identification_number = fields.Char(string='Identification Number', copy=True, store=True)
    insurance_subscription_number = fields.Char(string='Insurance Subscription Number', copy=True, store=True)
    labour_office_number = fields.Char(string='Labour Office Number', copy=True, store=True)
    location = fields.Text(string='Location', copy=True, store=True)
    registration_employee_number = fields.Integer(string='Registration Number', readonly=True)
    registration_number = fields.Char(string='Registration Number', help="""Identification number for the company""", copy=True, required=True, store=True)

    def get_employees_with_registration_number(self):
        pass
