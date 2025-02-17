from odoo import api, fields, models


class OtpConfirm(models.TransientModel):
    _name = 'otp.confirm'
    _description = 'Otp Confirm'

    rental_order_id = fields.Many2one(comodel_name='rental.contract', string='Rental Order', copy=True, store=True)

    def create_contract(self):
        pass
