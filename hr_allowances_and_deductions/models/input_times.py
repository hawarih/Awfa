from odoo import api, fields, models


class InputTimes(models.Model):
    _name = 'input.times'
    _description = 'Input Times'

    input_type_id = fields.Many2one(comodel_name='hr.payslip.input.type', string='Input Type', copy=True, store=True)
    rate = fields.Float(string='Rate', copy=True, required=True, store=True)
    repeat = fields.Selection(string='Repeat', selection=[('first', 'first'), ('second', 'second'), ('third', 'third'), ('fourth', 'fourth'), ('fifth', 'fifth')], copy=True, required=True, store=True)
