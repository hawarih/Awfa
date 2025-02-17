from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    accident_journal_id = fields.Many2one(comodel_name='account.journal', string='Journals')
    first_side_id = fields.Many2one(comodel_name='product.product', string='First Side')
    second_side_id = fields.Many2one(comodel_name='product.product', string='Second Side')
    third_side_id = fields.Many2one(comodel_name='product.product', string='Third Side')
