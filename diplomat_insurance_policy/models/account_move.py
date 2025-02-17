from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, store=True)
    is_insurance = fields.Boolean(string='Is Insurance', copy=True, store=True)
