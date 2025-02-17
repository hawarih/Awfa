from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    insurance_account_id = fields.Many2one(comodel_name='account.account', string='Insurance Account', copy=True, store=True)
    insurance_days = fields.Integer(string='Insurance Notification Days', copy=True, store=True)
    insurance_journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
