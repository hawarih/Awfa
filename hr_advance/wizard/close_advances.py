from odoo import api, fields, models


class CloseAdvances(models.TransientModel):
    _name = 'close.advances'
    _description = 'Close Advances'

    advance_ids = fields.Many2many(comodel_name='advance.salary', string='Advance', copy=True, readonly=True, relation='advance_salary_close_advances_rel', column1='close_advances_id', column2='advance_salary_id', store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, ondelete='cascade', store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, required=True, ondelete='cascade', store=True)
    remaining = fields.Float(string='Amount', copy=True, required=True, readonly=True, store=True)

    def close_advances(self):
        pass