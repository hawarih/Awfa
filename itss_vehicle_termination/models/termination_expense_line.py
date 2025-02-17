from odoo import api, fields, models


class TerminationExpenseLine(models.Model):
    _name = 'termination.expense.line'
    _description = 'Termination Expense Line'

    book_value = fields.Monetary(string='Book Value', copy=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, required=True, readonly=True, ondelete='restrict', store=True)
    credit_created = fields.Boolean(string='Credit Created', copy=True, store=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', related='company_id.currency_id', readonly=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    expense_id = fields.Many2one(comodel_name='account.asset', string='Expense', copy=True,  store=True)
    modify_action = fields.Selection(string='Modify Action', selection=[('dispose', 'Dispose'), ('sell', 'Sell'), ('modify', 'Re-evaluate'), ('pause', 'Pause')], copy=True, store=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', copy=True,  store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('pause', 'Paused'), ('confirm', 'Confirm')], store=True, default='draft')
    termination_id = fields.Many2one(comodel_name='vehicle.termination', string='Termination', copy=True,  store=True)

    def pause(self):
        pass

    def create_credit(self):
        pass

    def sell_dispose(self):
        pass
