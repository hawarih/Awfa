from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    approval_code = fields.Char(string='Approval Code', copy=True, readonly=True, store=True)
    journal_method_id = fields.Many2one(comodel_name='journal.payment.method', string='Journal Payment Method', copy=True, readonly=True, store=True)
