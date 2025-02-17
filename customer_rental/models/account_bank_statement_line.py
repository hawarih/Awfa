from odoo import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, related='move_id.rental_contract_id')
