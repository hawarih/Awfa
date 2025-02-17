from odoo import api, fields, models


class HrAbsenceRule(models.Model):
    _name = 'hr.absence.rule'
    _description = 'Hr Absence Rule'

    line_ids = fields.One2many(comodel_name='hr.absence.rule.line', inverse_name='absence_id', string='Late In Periods', store=True)
    name = fields.Char(string='name', copy=True, required=True, translate=True, store=True)
