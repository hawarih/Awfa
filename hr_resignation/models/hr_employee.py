from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    analytic_account_id = fields.Many2one(comodel_name='account.analytic.account', string='Analytic Account', copy=True, ondelete='set null', store=True)
    fired = fields.Boolean(string='Fired', help="""If checked then employee has fired""", copy=True, store=True)
    resign_date = fields.Date(string='Resign Date', help="""Date of the resignation""", copy=True, readonly=True, store=True)
    resigned = fields.Boolean(string='Resigned', help="""If checked then employee has resigned""", copy=True, store=True)
