from odoo import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    purchase = fields.Many2one(comodel_name='purchase.order', string='Purchase', copy=True, related='move_id.purchase')
