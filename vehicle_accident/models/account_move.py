from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    accidents_lines_id = fields.Many2one(comodel_name='vehicle.accident.lines', string='Accidents Lines', copy=True, store=True)

    def action_post(self):
        self.state = 'posted'
        