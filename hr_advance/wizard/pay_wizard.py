from odoo import api, fields, models


class PayWizard(models.TransientModel):
    _name = 'pay.wizard'
    _description = 'Pay Wizard'

    advance_id = fields.Many2one(comodel_name='advance.salary', string='Advance Salary', copy=True, required=True, ondelete='cascade', store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, ondelete='cascade', store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', related='advance_id.employee_id', required=True, readonly=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, required=True, ondelete='cascade', store=True)
    payment_date = fields.Date(string='Payment Date', copy=True, required=True, store=True)
    remaining = fields.Float(string='Amount', related='advance_id.remaining', readonly=True)

    def action_pay(self):
        pass