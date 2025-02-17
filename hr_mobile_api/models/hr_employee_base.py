from odoo import api, fields, models


class HrEmployeeBase(models.AbstractModel):
    _inherit = 'hr.employee.base'

    fcm_token = fields.Char(string='Fcm Token', copy=True, store=True)
