from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    accidents_lines_id = fields.Many2one(comodel_name='vehicle.accident.lines', string='Accidents Lines', copy=True, related='move_id.accidents_lines_id')
