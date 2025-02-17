from odoo import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    termination_id = fields.Many2one(comodel_name='vehicle.termination', string='Termination', copy=True, related='move_id.termination_id')
