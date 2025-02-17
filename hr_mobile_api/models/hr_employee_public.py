from odoo import api, fields, models


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    fcm_token = fields.Char(string='Fcm Token', copy=True, store=True)
