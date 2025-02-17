from odoo import api, fields, models


class DelayDueAmountLines(models.TransientModel):
    _name = 'delay.due.amount.lines'
    _description = 'Delay Due Amount Lines'

    amount = fields.Float(string='Amount', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, store=True)
    rental_fine_wizard = fields.Many2one(comodel_name='customer.rental.fine.wizard', string='Rental Fine Wizard', copy=True, store=True)
