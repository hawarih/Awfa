from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    installment_batch_payment_id = fields.Many2one(comodel_name='installment.batch.payment', string='Installment Batch Payment', copy=True, store=True)
