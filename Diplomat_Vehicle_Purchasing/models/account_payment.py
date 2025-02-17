from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    purchase = fields.Many2one(comodel_name='purchase.order', string='Purchase', copy=True, related='move_id.purchase')
    purchase_order_id = fields.Many2one(comodel_name='purchase.order', string='Purchase Order', copy=True, ondelete='set null', store=True)
