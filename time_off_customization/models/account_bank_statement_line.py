from odoo import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    completion_id = fields.Many2one(comodel_name='hr.leave.completion', string='Completion', copy=True, related='move_id.completion_id')
