from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ovt_holidays_rate = fields.Float(string='OVT Holidays Rate', copy=True, store=True)
    ovt_working_days_rate = fields.Float(string='OVT Working Days Rate', copy=True, store=True)
