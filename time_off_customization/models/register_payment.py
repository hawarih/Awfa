from odoo import api, fields, models


class RegisterPayment(models.TransientModel):
    _name = 'register.payment'
    _description = 'Register Payment'

    amount = fields.Float(string='Amount', copy=True, store=True)
    completion_id = fields.Many2one(comodel_name='hr.leave.completion', string='completion', copy=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    final_amount = fields.Float(string='Final Amount', copy=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    memo = fields.Char(string='Memo', copy=True, store=True)
    payment_method_line_id = fields.Many2one(comodel_name='account.payment.method.line', string='Payment Method Line', readonly=True)
    type = fields.Selection(string='Type', selection=[('entry', 'Entry'), ('payment', 'Payment'), ('contract_payment', 'Contract Payment')], copy=True, store=True)
    vehicle_contract_line_id = fields.Many2one(comodel_name='_unknown', string='Vehicle Contract Line', copy=True, store=True)
    vendor_id = fields.Many2one(comodel_name='res.partner', string='Employee', copy=True, store=True)

    def create_payment(self):
        pass
