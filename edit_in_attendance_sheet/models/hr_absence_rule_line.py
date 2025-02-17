from odoo import api, fields, models


class HrAbsenceRuleLine(models.Model):
    _inherit = 'hr.absence.rule.line'

    day_period = fields.Selection(string='Day Period', selection=[('morning', 'Morning'), ('afternoon', 'Afternoon')], copy=True, store=True)

    _sql_constraints = [
        ('hr_absence_rule_line_absence_rule_cons', 'unique(absence_id,counter,day_period)', 'The counter Must Be unique Per Rule')
    ]