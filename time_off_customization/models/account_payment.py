from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    completion_id = fields.Many2one(comodel_name='hr.leave.completion', string='Completion', copy=True, related='move_id.completion_id')
