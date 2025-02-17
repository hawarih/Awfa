from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    fcm_token = fields.Char(string='Fcm Token', copy=True, store=True)
