from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    commission = fields.Boolean(string='Commission', copy=True, store=True)
    contract_type = fields.Selection(string='Contract Type', selection=[('permanent', 'Permanent'), ('trainee', 'Trainee'), ('contract', 'Contract')], copy=True, store=True)
    kafala = fields.Float(string='Kafala', copy=True, store=True)
