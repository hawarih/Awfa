from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    leave_days = fields.Float(string='Leave Days', copy=True, store=True)
