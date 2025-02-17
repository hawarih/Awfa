from odoo import api, fields, models


class PettyCashType(models.Model):
    _name = 'petty.cash.type'
    _description = 'Petty Cash Type'

    adj_date = fields.Date(string='Adjustment Date', copy=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, required=True, ondelete='restrict', store=True)
    date = fields.Date(string='Payment Date', copy=True, store=True)
    force_date = fields.Boolean(string='Force Adjustment Date', copy=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Petty Cash Journal', copy=True, store=True)
    move_group = fields.Boolean(string='Group Journal Entries', copy=True, store=True)
    name = fields.Char(string='name', store=True)
    reference = fields.Char(string='Reference', copy=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('confirm', 'Confirmed')], default='draft', store=True)
    type = fields.Selection(string='Type', selection=[('temp', 'Temporary'), ('per', 'Permanent')], store=True)

    def action_confirm(self):
                pass

    def action_draft(self):
                pass