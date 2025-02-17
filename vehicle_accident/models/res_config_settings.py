from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_accident_journal_id = fields.Many2one(comodel_name='account.journal', string='Journals', related='company_id.accident_journal_id', store=True, readonly=False)
    company_first_side_id = fields.Many2one(comodel_name='product.product', string='First Side', related='company_id.first_side_id',store=True, readonly=False )
    company_second_side_id = fields.Many2one(comodel_name='product.product', string='Second Side', related='company_id.second_side_id', store=True, readonly=False)
    company_third_side_id = fields.Many2one(comodel_name='product.product', string='Third Side', related='company_id.third_side_id', store=True, readonly=False)
