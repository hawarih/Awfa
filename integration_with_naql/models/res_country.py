from odoo import api, fields, models


class ResCountry(models.Model):
    _inherit = 'res.country'

    naql_id = fields.Char(string='Naql', copy=True, store=True)
    yakeen_code = fields.Char(string='Yakeen Code', copy=True, store=True)
