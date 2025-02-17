from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    insurance_line_id = fields.Many2one(comodel_name='insurance.policy.line', string='Insurance Line', copy=True, store=True)
