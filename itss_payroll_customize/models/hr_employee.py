from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    difference = fields.Integer(string='Difference', copy=True, store=True)
    join_this_month = fields.Boolean(string='Join This Month', readonly=True)
    saudi = fields.Boolean(string='Saudi', readonly=True, store=True)
