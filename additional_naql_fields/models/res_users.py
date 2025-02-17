from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    operator_id = fields.Integer(string='Operator-ID', copy=True, store=True)
    passport_number = fields.Char(string='Passport Number', copy=True, related='partner_id.passport_number')
