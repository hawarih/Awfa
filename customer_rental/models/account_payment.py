from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, related='move_id.rental_contract_id')
