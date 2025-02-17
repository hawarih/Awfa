from odoo import api, fields, models


class HrLateRule(models.Model):
    _name = 'hr.late.rule'
    _description = 'Hr Late Rule'

    line_ids = fields.One2many(comodel_name='hr.late.rule.line', inverse_name='late_id', string='Late In Periods', store=True)
    name = fields.Char(string='name', copy=True, required=True, translate=True, store=True)
