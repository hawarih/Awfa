from odoo import api, fields, models


class HrPayrollStructure(models.Model):
    _inherit = 'hr.payroll.structure'

    is_eos = fields.Boolean(string='EOS Structure', copy=True, store=True)
