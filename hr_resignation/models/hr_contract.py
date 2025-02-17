from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    analytic_account_id = fields.Many2one(comodel_name='account.analytic.account', string='Analytic Account', related='employee_id.analytic_account_id', readonly=True)
