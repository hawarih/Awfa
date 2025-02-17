from odoo import api, fields, models


class PartnerConfigAccount(models.Model):
    _name = 'partner.config.account'
    _description = 'Partner Config Account'

    name = fields.Char(string='Name', copy=True, required=True, store=True)
    property_account_payable_id = fields.Many2one(comodel_name='account.account', string='Account Payable', help="""This account will be used instead of the default one as the payable account for the current partner""", required=True, ondelete='restrict')
    property_account_receivable_id = fields.Many2one(comodel_name='account.account', string='Account Receivable', help="""This account will be used instead of the default one as the receivable account for the current partner""", required=True, ondelete='restrict')
    type = fields.Selection(string='Type', selection=[('person', 'Individual'), ('company', 'Company')], copy=True, required=True, store=True)
