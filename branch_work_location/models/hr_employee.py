from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    check_type = fields.Selection(string='Attendance Type', selection=[('work', 'Work Location'), ('restrict', 'Any Work Location'), ('any', 'Any Where')], copy=True, store=True)
