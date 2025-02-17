from odoo import api, fields, models


class PettyPayInvoiceWizard(models.TransientModel):
    _name = 'petty.pay.invoice.wizard'
    _description = 'Petty Pay Invoice Wizard'

    amount = fields.Monetary(string='Payment Amount', copy=True, required=True, store=True)
    balance = fields.Monetary(string='Balance', readonly=True)
    communication = fields.Char(string='Memo', copy=True, store=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', copy=True, required=True, ondelete='cascade', store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True, store=True)
    invoice_id = fields.Many2one(comodel_name='account.move', string='Invoice', copy=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Payment Method', readonly=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', copy=True, store=True)
    payment_method_id = fields.Many2one(comodel_name='account.payment.method', string='Payment Type', copy=True, required=True, ondelete='cascade', store=True)
    petty_cash_ids = fields.Many2many(comodel_name='petty.cash', string='Petty Cash', copy=True, relation='petty_cash_petty_pay_invoice_wizard_rel', column1='petty_pay_invoice_wizard_id', column2='petty_cash_id', store=True)
    petty_id = fields.Many2one(comodel_name='petty.cash', string='Petty Cash', copy=True, store=True)

    def petty_invoice_post_payment(self):
        pass