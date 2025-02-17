from odoo import api, fields, models


class CancelArrestWarrant(models.Model):
    _name = 'cancel.arrest.warrant'
    _description = 'Cancel Arrest Warrant'

    cancellation_number = fields.Integer(string='Cancellation Number', copy=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    notes = fields.Text(string='Notes', copy=True, store=True)
    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)
