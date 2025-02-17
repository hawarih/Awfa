from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    partner_category_id = fields.Many2many(comodel_name='res.partner.category', string='Partner Tags', readonly=True, relation='account_move_line_res_partner_category_rel', column1='account_move_line_id', column2='res_partner_category_id', store=True)
    partner_group_id = fields.Many2one(comodel_name='res.partner', string='Partner Group', readonly=True, store=True)
    petty_cash_ids = fields.Many2many(comodel_name='petty.cash', string='Petty Cash', copy=True, relation='rel_petty_move', column1='petty_cash', column2='petty_pement', store=True)
    petty_id = fields.Many2one(comodel_name='petty.cash', string='Petty Cash', copy=True, store=True)
    petty_partner_id = fields.Many2one(comodel_name='res.partner', string='Petty Partner', copy=True, store=True)
