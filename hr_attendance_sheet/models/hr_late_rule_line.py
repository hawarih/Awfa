from odoo import api, fields, models


class HrLateRuleLine(models.Model):
    _name = 'hr.late.rule.line'
    _description = 'Hr Late Rule Line'

    amount = fields.Float(string='Amount', copy=True, store=True)
    fifth = fields.Float(string='Fifth Time', copy=True, store=True)
    first = fields.Float(string='First Time', copy=True, store=True)
    fourth = fields.Float(string='Fourth Time', copy=True, store=True)
    late_id = fields.Many2one(comodel_name='hr.late.rule', string='Late Rule', copy=True, store=True)
    rate = fields.Float(string='Rate', copy=True, store=True)
    second = fields.Float(string='Second Time', copy=True, store=True)
    third = fields.Float(string='Third Time', copy=True, store=True)
    time = fields.Float(string='Time', copy=True, store=True)
    type = fields.Selection(string='Type', selection=[('fix', 'Fixed'), ('rate', 'Rate')], copy=True, required=True, store=True)
