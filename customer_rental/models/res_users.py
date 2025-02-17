from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    allow_multi_contract = fields.Boolean(string='Allow Multi Contract', copy=True, store=True)
