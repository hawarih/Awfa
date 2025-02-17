from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    termination_id = fields.Many2one(comodel_name='vehicle.termination', string='Termination', copy=True, related='move_id.termination_id')
