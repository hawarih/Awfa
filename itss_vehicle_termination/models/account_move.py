from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    termination_id = fields.Many2one(comodel_name='vehicle.termination', string='Termination', copy=True,  store=True)
