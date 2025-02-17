from odoo import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, related='move_id.insurance_id')
    is_insurance = fields.Boolean(string='Is Insurance', copy=True, related='move_id.is_insurance')
