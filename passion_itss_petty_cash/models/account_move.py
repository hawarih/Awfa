from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    employee_id = fields.Many2one(comodel_name='hr.employee', string='Responsible Employee', copy=True, store=True)

    def petty_inv_pay(self):
        pass
