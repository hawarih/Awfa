from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    employee_id = fields.Many2one(comodel_name='hr.employee', string='Responsible Employee', copy=True, related='move_id.employee_id')
    petty_cash_ids = fields.Many2many(comodel_name='petty.cash', string='Petty Cash', copy=True, relation='rel_petty_pement', column1='petty_cash', column2='petty_pement', store=True)
    petty_id = fields.Many2one(comodel_name='petty.cash', string='Petty Cash', copy=True, store=True)

    def action_post(self):
        self.write({'state': 'posted'})
        

