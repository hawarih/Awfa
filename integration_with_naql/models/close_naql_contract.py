from odoo import api, fields, models


class CloseNaqlContract(models.TransientModel):
    _name = 'close.naql.contract'
    _description = 'Close Naql Contract'

    main_close_code_id = fields.Many2one(comodel_name='naql.main.close.code', string='Close Reason', copy=True, required=True, ondelete='cascade', store=True)
    oil_change_cost = fields.Float(string='Oil Change Cost', copy=True, store=True)
    sub_close_code_id = fields.Many2one(comodel_name='naql.sub.close.code', string='Sub Reason', copy=True, required=True, ondelete='cascade', store=True)

    def action_apply(self):
        pass
