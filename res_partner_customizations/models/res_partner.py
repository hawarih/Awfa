from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    account = fields.Many2one(comodel_name='account.account', string='Account', copy=True, store=True)
    accounting_page_group = fields.Boolean(string='Accounting Page Group', readonly=True)
    age = fields.Char(string='Age', readonly=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, index=True, store=True)
    company_type = fields.Selection(string='Company Type', selection=[('person', 'Individual'), ('company', 'Company')])
    customer = fields.Boolean(string='Is Customer', copy=True, store=True)
    customized_mobile = fields.Char(string='Mobile', copy=True, store=True)
    mobile = fields.Char(string='Mobile', related='customized_mobile', readonly=True)
    sales_purchases_group = fields.Boolean(string='Sales Purchases Group', readonly=True)
