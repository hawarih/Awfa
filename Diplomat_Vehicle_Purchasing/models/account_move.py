from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    purchase = fields.Many2one(comodel_name='purchase.order', string='Purchase', copy=True, ondelete='set null', store=True)
