from odoo import api, fields, models


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    resignation_id = fields.Many2one(comodel_name='hr.resignation', string='Resignation Request', copy=True, ondelete='set null', store=True)
