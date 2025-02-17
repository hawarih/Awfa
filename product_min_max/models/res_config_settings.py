from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    user_ids = fields.Many2many(comodel_name='res.users', string='Accepted Users', related='company_id.user_ids')
