from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    notice_days = fields.Integer(string='Notice Period', copy=True, store=True)
