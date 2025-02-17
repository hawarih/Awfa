from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    time_off_allowance = fields.Float(string='Time off Allowance', copy=True, store=True, )
    time_off_ticket = fields.Float(string='Ticket Rate', copy=True, store=True, )
