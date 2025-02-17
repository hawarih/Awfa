from odoo import api, fields, models


class BatchInternalTransferLine(models.Model):
    _inherit = 'batch.internal.transfer.line'

    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, default=lambda self: self.env.user.company_id,
                                 required=True, readonly=True, ondelete='restrict', store=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', related='company_id.currency_id', required=True, readonly=True)
    word_num = fields.Char(string='Amount In Words:', readonly=True, translate=True)
