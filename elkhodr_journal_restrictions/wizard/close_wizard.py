from odoo import api, fields, models


class CloseWizard(models.TransientModel):
    _inherit = 'close.wizard'

    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, required=True, ondelete='cascade', store=True)
