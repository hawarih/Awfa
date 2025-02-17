from odoo import api, fields, models


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    request_date_from_period = fields.Selection(string='Date Period Start', selection=[('am', 'First Half'), ('pm', 'Second Half')], copy=True, store=True)
