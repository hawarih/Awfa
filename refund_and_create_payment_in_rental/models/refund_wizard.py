from odoo import api, fields, models


class RefundWizard(models.TransientModel):
    _name = 'refund.wizard'
    _description = 'Refund Wizard'

    amount = fields.Float(string='Amount', copy=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    memo_rel = fields.Char(string='Memo', copy=True, store=True)
    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)

    def button_pay(self):
        pass