from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    account = fields.Many2one(comodel_name='account.account', string='Account', copy=True, related='partner_id.account')
    accounting_page_group = fields.Boolean(string='Accounting Page Group', related='partner_id.accounting_page_group', readonly=True)
    age = fields.Char(string='Age', related='partner_id.age', readonly=True)
    company_type = fields.Selection(string='Company Type', selection=[], related='partner_id.company_type')
    customer = fields.Boolean(string='Is Customer', copy=True, related='partner_id.customer')
    customized_mobile = fields.Char(string='Mobile', copy=True, related='partner_id.customized_mobile')
    mobile = fields.Char(string='Mobile', related='partner_id.mobile', readonly=True)
    sales_purchases_group = fields.Boolean(string='Sales Purchases Group', related='partner_id.sales_purchases_group', readonly=True)
