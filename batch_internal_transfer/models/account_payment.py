from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    batch_internal_transfer_id = fields.Many2one(comodel_name='batch.internal.transfer', string='Batch Internal Transfer', copy=True, store=True)
