from odoo import api, fields, models


class ActionClosed(models.TransientModel):
    _name = 'action.closed'
    _description = 'Action Closed'

    note = fields.Char(string='Note', copy=True, store=True)
    transfer_id = fields.Many2one(comodel_name='ywt.internal.stock.transfer', string='Transfer', copy=True, store=True)

    def action_for_closed(self):
        pass
