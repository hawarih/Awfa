from odoo import api, fields, models


class HrOtherAllowanceLine(models.Model):
    _name = 'hr.other.allowance.line'
    _description = 'Hr Other Allowance Line'

    amount = fields.Float(string='Amount', copy=True, store=True)
    code = fields.Char(string='Code', copy=True, required=True, store=True)
    contract_id = fields.Many2one(comodel_name='hr.contract', string='Contract', copy=True, store=True)
    hr_other_allowance_id = fields.Many2one(comodel_name='hr.other.allowance', string='Name', copy=True, store=True)
