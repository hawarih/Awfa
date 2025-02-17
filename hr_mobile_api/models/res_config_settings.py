from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    fcm_authorization = fields.Char(string='Fcm Authorization', copy=True, store=True)
    fcm_url = fields.Char(string='Fcm Url', copy=True, store=True)
    mobile_terms_policy_id = fields.Many2one(comodel_name='mobile.terms.policy', string='Mobile Terms & Policy', copy=True,  store=True)
