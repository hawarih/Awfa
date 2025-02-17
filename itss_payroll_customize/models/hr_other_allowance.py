from odoo import api, fields, models


class HrOtherAllowance(models.Model):
    _name = 'hr.other.allowance'
    _description = 'Hr Other Allowance'

    amount = fields.Float(string='Amount', copy=True, store=True)
    code = fields.Char(string='Code', copy=True, required=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
