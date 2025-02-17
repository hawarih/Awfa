from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)
