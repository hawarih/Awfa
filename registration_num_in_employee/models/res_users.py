from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_work_address = fields.Boolean(string='Is Work Address', copy=True, related='partner_id.is_work_address')
