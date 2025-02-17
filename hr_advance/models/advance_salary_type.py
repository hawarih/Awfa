from odoo import api, fields, models


class AdvanceSalaryType(models.Model):
    _name = 'advance.salary.type'
    _description = 'Advance Salary Type'

    credit_account_id = fields.Many2one(comodel_name='account.account', string='Credit Account', copy=True, required=True, ondelete='restrict', store=True)
    debit_account_id = fields.Many2one(comodel_name='account.account', string='Debit Account', copy=True, required=True, ondelete='restrict', store=True)
    name = fields.Char(string='Name', copy=True, required=True, store=True)
