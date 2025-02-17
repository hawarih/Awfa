from odoo import api, fields, models


class InsurancePolicyLine(models.Model):
    _inherit = 'insurance.policy.line'

    customer_deductible = fields.Float(string='Customer Deductible', copy=True, store=True)
