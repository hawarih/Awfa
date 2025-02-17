from odoo import api, fields, models


class CreatePaymentWizard(models.TransientModel):
    _name = 'create.payment.wizard'
    _description = 'Create Payment Wizard'

    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)

    def create_payment(self):
        pass
