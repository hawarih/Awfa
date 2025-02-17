from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    maintenance_id = fields.Many2one(comodel_name='maintenance.request', string='Maintenance', copy=True,  store=True)
