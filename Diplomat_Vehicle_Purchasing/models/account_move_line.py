from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    plates_fee = fields.Float(string='Plates Fee', copy=True, store=True)
