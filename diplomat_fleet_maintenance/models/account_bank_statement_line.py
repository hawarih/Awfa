from odoo import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    maintenance_id = fields.Many2one(comodel_name='maintenance.request', string='Maintenance', copy=True, related='move_id.maintenance_id')
