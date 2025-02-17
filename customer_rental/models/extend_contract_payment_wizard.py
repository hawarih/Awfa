from odoo import api, fields, models


class ExtendContractPaymentWizard(models.TransientModel):
    _name = 'extend.contract.payment.wizard'
    _description = 'Extend Contract Payment Wizard'

    contract_id = fields.Many2one(comodel_name='rental.contract', string='Contract', copy=True, store=True)
    journal = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, store=True)
    to_pay = fields.Float(string='To Pay', copy=True, store=True)

    def confirm_payment(self):
        pass