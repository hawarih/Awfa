from odoo import api, fields, models


class AccountAnalyticPlan(models.Model):
    _inherit = 'account.analytic.plan'

    link_with_vehicle = fields.Boolean(string='Link With Vehicle', copy=True, store=True)
