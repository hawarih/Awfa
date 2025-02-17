from odoo import api, fields, models


class HrAbsenceRuleLine(models.Model):
    _name = 'hr.absence.rule.line'
    _description = 'Hr Absence Rule Line'

    absence_id = fields.Many2one(comodel_name='hr.absence.rule', string='name', copy=True, store=True)
    counter = fields.Selection(string='Times', selection=[('1', 'First Time'), ('2', 'Second Time'), ('3', 'Third Time'), ('4', 'Fourth Time'), ('5', 'Fifth Time')], copy=True, required=True, store=True)
    rate = fields.Float(string='Rate', copy=True, required=True, store=True)

    
    _sql_constraints = [
        ('absence_id_counter_uniq', 'unique(absence_id, counter)', 'The counter Must Be unique Per Rule'),
    ]