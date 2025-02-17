from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    account_analytic_account_ids = fields.Many2many(comodel_name='account.analytic.account', string='Account Analytic Account', copy=True, relation='account_analytic_account_res_users_rel', column1='res_users_id', column2='account_analytic_account_id', store=True)
    account_analytic_plan_ids = fields.Many2many(comodel_name='account.analytic.plan', string='Account Analytic Plan', copy=True, relation='account_analytic_plan_res_users_rel', column1='res_users_id', column2='account_analytic_plan_id', store=True)
    journal_ids = fields.Many2many(comodel_name='account.journal', string='Journal', copy=True, relation='journal_journal', column1='journal_id1', column2='journal_id4', store=True)
    miscellaneous_journal_ids = fields.Many2many(comodel_name='account.journal', string='Miscellaneous Journal', copy=True, relation='miscellaneous_journal', column1='miscellaneous_id', column2='journal_id3', store=True)
    purchase_journal_ids = fields.Many2many(comodel_name='account.journal', string='Purchase Journal', copy=True, relation='purchase_journal', column1='purchase_id', column2='journal_id2', store=True)
    sales_journal_ids = fields.Many2many(comodel_name='account.journal', string='Sales Journal', copy=True, relation='sale_journal', column1='sale_id', column2='journal_id1', store=True)
    transfer_to_ids = fields.Many2many(comodel_name='account.journal', string='Transfer To', copy=True, relation='transfer_journal', column1='transfer_id1', column2='journal_id5', store=True)
