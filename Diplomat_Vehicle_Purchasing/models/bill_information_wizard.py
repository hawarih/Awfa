from odoo import api, fields, models


class BillInformationWizard(models.TransientModel):
    _name = 'bill.information.wizard'
    _description = 'Bill Information Wizard'

    cash_purchasing = fields.Boolean(string='Cash Purchasing', copy=True, store=True)
    installment_date = fields.Date(string='First Installment Date', copy=True, store=True)
    interest_amount = fields.Float(string='Interest Amount', copy=True, store=True)
    is_leasing = fields.Boolean(string='Is Leasing', copy=True, store=True)
    no_months = fields.Integer(string='No of Months Without Interest', copy=True, store=True)
    number_installment = fields.Integer(string='Number of Installment', copy=True, store=True)
    start_date = fields.Date(string='Contract Start Date', copy=True, store=True)
    vehicle_ids = fields.One2many(comodel_name='purchase.data', inverse_name='purchase_id', string='Bill Information', store=True)

    def action_confirm(self):
        pass