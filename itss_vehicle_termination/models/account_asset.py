from odoo import api, fields, models


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    termination_id = fields.Many2one(comodel_name='vehicle.termination', string='Termination', copy=True,  store=True)
