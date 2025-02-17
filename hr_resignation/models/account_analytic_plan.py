from odoo import api, fields, models


class AccountAnalyticPlan(models.Model):
    _inherit = 'account.analytic.plan'

    link_with_employee = fields.Boolean(string='Link With Employee', copy=True, store=True)
