from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    date_end_hijri = fields.Char(string='Contract End Hijri Date', readonly=True)
    date_start_hijri = fields.Char(string='Contract Start Hijri Date', readonly=True)
    hr_shifts = fields.Many2many(comodel_name='hr.department.shift.lines', string='Shifts', related='employee_id.hr_shifts', readonly=True)
