from odoo import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    employee_id = fields.Many2one(comodel_name='hr.employee', string='Responsible Employee', copy=True, related='move_id.employee_id')
