from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    termination_account_id = fields.Many2one(comodel_name='account.account', string='Termination Account', copy=True,  store=True)
    termination_journal_id = fields.Many2one(comodel_name='account.journal', string='Termination Journal', copy=True,  store=True)
