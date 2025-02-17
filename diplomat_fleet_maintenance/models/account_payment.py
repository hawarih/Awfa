from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    maintenance_id = fields.Many2one(comodel_name='maintenance.request', string='Maintenance', copy=True, related='move_id.maintenance_id')
