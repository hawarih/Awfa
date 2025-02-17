from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_work_address = fields.Boolean(string='Is Work Address', copy=True, store=True)
