from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    payment_method_id = fields.Many2one(comodel_name='account.payment.method', string='Payment Method Type', related='payment_method_line_id.payment_method_id', readonly=True, store=True)
