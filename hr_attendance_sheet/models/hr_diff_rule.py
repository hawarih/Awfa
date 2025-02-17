from odoo import api, fields, models


class HrDiffRule(models.Model):
    _name = 'hr.diff.rule'
    _description = 'Hr Diff Rule'

    line_ids = fields.One2many(comodel_name='hr.diff.rule.line', inverse_name='diff_id', string='Difference time Periods', store=True)
    name = fields.Char(string='name', copy=True, required=True, translate=True, store=True)
