from odoo import api, fields, models


class HrOvertimeRule(models.Model):
    _name = 'hr.overtime.rule'
    _description = 'Hr Overtime Rule'

    active_after = fields.Float(string='Apply after', help="""After this time the overtime will be calculated""", copy=True, store=True)
    name = fields.Char(string='name', copy=True, store=True)
    rate = fields.Float(string='Rate', copy=True, store=True)
    type = fields.Selection(string='Type', selection=[('weekend', 'Week End'), ('workday', 'Working Day'), ('ph', 'Public Holiday')], copy=True, store=True)
