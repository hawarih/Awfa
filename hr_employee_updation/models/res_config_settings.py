from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    no_of_days = fields.Integer(string='No Of Days', copy=True, store=True)
    notice_period = fields.Boolean(string='Notice Period', copy=True, store=True)
