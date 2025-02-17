from odoo import api, fields, models


class SuspendNaqlContract(models.TransientModel):
    _name = 'suspend.naql.contract'
    _description = 'Suspend Naql Contract'

    damage_cost = fields.Float(string='Damage Cost', copy=True, store=True)
    oil_change_cost = fields.Float(string='Oil Change Cost', copy=True, store=True)
    spare_parts_cost = fields.Float(string='Spare Parts Cost', copy=True, store=True)
    suspend_code_id = fields.Many2one(comodel_name='naql.suspend.code', string='Suspend Reason', copy=True, required=True, ondelete='cascade', store=True)

    def action_apply(self):
        pass
