from odoo import api, fields, models


class HrResignationReasonRule(models.Model):
    _name = 'hr.resignation.reason.rule'
    _description = 'Hr Resignation Reason Rule'

    calculation_factor = fields.Float(string='Calculation Factor', copy=True, required=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, ondelete='set null', store=True)
    period_from = fields.Float(string='Period Of Service From(Months)', copy=True, required=True, store=True)
    period_to = fields.Float(string='Period Of Service To(Months)', copy=True, required=True, store=True)
    reason_id = fields.Many2one(comodel_name='hr.resignation.reason', string='Resignation Reason', copy=True, ondelete='cascade', store=True)
    reward_ration = fields.Float(string='Reward Ratio(1/Reward Ratio)', help="""Reward Ration will be 1/User input for eg. 1/3 incase employee resignation and years is equal 5""", copy=True, store=True)
    rule_ids = fields.Many2many(comodel_name='hr.salary.rule', string='Calculation Salary Rules', copy=True, relation='resignation_salary_rule_rel', column1='res_id', column2='rule_id', store=True)
    sequence = fields.Integer(string='Sequence', copy=True, store=True)
