from odoo import api, fields, models


class ExtendWizard(models.TransientModel):
    _name = 'extend.wizard'
    _description = 'Extend Wizard'

    accepted_extended_days = fields.Integer(string='Accepted Extended Days', readonly=True)
    contract_id = fields.Many2one(comodel_name='rental.contract', string='Contract', copy=True, store=True)
    current_date = fields.Date(string='Date', copy=True, store=True)
    current_due_amount = fields.Float(string='Current Due Amount', readonly=True)
    extended_days = fields.Integer(string='Extended Days', copy=True, store=True)
    journal = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    memo = fields.Char(string='Memo', related='contract_id.name', readonly=True, translate=True)
    name = fields.Char(string='Name', copy=True, store=True)
    paid_amount = fields.Float(string='Paid Amount ( Trip Days Only )', readonly=True)
    to_pay = fields.Float(string='To Pay', copy=True, store=True)
    total_payment = fields.Float(string='Total Payment', readonly=True)

    def extend_button(self):
        pass