from odoo import api, fields, models


class ExtendWizard(models.TransientModel):
    _inherit = 'extend.wizard'

    opt_value = fields.Char(string='Opt Value', copy=True, required=True, store=True)
