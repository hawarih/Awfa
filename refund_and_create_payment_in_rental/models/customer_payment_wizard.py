from odoo import api, fields, models


class CustomerPaymentWizard(models.TransientModel):
    _name = 'customer.payment.wizard'
    _description = 'Customer Payment Wizard'

    amount = fields.Float(string='Amount', copy=True, store=True)
    approval_code = fields.Char(string='Approval Code', copy=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    enable_payment_method = fields.Boolean(string='Work With Payment Methods', related='journal_id.enable_payment_method', readonly=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    journal_payment_method = fields.Many2one(comodel_name='journal.payment.method', string='Journal Payment Method', copy=True, store=True)
    memo_rel = fields.Char(string='Memo', copy=True, store=True)
    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)

    def button_pay(self):
        pass