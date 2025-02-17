from odoo import api, fields, models


class BatchInternalTransfer(models.Model):
    _inherit = 'batch.internal.transfer'

    company_id = fields.Many2one(comodel_name='res.company', string='Company',default=lambda self: self.env.user.company_id,
                                copy=True, required=True, readonly=True, ondelete='restrict', store=True)
    description = fields.Char(string='Description', copy=True, store=True)

    def action_print(self):
        pass