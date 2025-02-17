from odoo import api, fields, models


class Statement(models.Model):
    _name = 'statement'
    _description = 'Statement'

    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)
    statement = fields.Text(string='Statement', copy=True, store=True)
