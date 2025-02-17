from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    passport_number = fields.Char(string='Passport Number', copy=True, store=True)
