from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    partner_config_account_id = fields.Many2one(comodel_name='partner.config.account', string='Partner Config Account', copy=True, related='partner_id.partner_config_account_id')
