from odoo import api, fields, models


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, store=True)
