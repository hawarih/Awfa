from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    app_auth = fields.Char(string='App Auth', copy=True, store=True)
    app_id = fields.Char(string='App', copy=True, store=True)
    app_key = fields.Char(string='App Key', copy=True, store=True)
    is_production = fields.Boolean(string='Is Production', copy=True, store=True)
    url_production = fields.Char(string='Url Production', copy=True, store=True)
    url_staging = fields.Char(string='Url Staging', copy=True, store=True)
