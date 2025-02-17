from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, related='move_id.insurance_id')
    is_insurance = fields.Boolean(string='Is Insurance', copy=True, related='move_id.is_insurance')
