from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    completion_id = fields.Many2one(comodel_name='hr.leave.completion', string='Completion', copy=True, store=True)
