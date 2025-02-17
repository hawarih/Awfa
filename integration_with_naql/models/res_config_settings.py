from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_auth = fields.Char(string='App Auth', related='company_id.app_auth')
    app_id = fields.Char(string='App', related='company_id.app_id')
    app_key = fields.Char(string='App Key', related='company_id.app_key')
    is_production = fields.Boolean(string='Is Production', related='company_id.is_production')
    url_production = fields.Char(string='Url Production', related='company_id.url_production')
    url_staging = fields.Char(string='Url Staging', related='company_id.url_staging')
