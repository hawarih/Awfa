from odoo import api, fields, models


class NaqlCreateContract(models.TransientModel):
    _name = 'naql.create.contract'
    _description = 'Naql Create Contract'

    otp = fields.Char(string='Otp', copy=True, store=True)

    def action_create_contract(self):
        pass