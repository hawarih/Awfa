from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    bypass_intermediate_account = fields.Boolean(string='Bypass Intermediate Account', copy=True, store=True)
