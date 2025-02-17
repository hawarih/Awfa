from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_config_account_id = fields.Many2one(comodel_name='partner.config.account', string='Partner Config Account', copy=True, store=True)
