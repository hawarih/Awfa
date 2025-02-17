from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
