from odoo import api, fields, models


class PayAdvanceLine(models.Model):
    _name = 'pay.advance.line'
    _description = 'Pay Advance Line'

    advance_id = fields.Many2one(comodel_name='advance.salary', string='Advance', copy=True, store=True)
    amount = fields.Float(string='Amount', copy=True, store=True)
    due_date = fields.Date(string='Due date', copy=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', related='advance_id.employee_id', readonly=True, store=True)
    is_post = fields.Boolean(string='post', copy=True, store=True)

    def action_close_advance(self):
        pass