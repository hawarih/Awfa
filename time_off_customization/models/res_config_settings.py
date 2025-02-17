from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allowance_account_id = fields.Many2one(comodel_name='account.account', string='Time off Allowance', copy=True, store=True)
    allowance_journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    benefits_allowance_account_id = fields.Many2one(comodel_name='account.account', string='Time off Benefits', copy=True, store=True)
    other_allowance_account_id = fields.Many2one(comodel_name='account.account', string='Time off Other Allowance', copy=True, store=True)
    ticket_allowance_account_id = fields.Many2one(comodel_name='account.account', string='Time off Ticket', copy=True, store=True)
