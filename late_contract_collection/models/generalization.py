from odoo import api, fields, models


class Generalization(models.Model):
    _name = 'generalization'
    _description = 'Generalization'

    date = fields.Date(string='Date', copy=True, store=True)
    follower = fields.Many2one(comodel_name='hr.employee', string='Follower', copy=True, store=True)
    generalization_number = fields.Integer(string='Generalization Number', copy=True, store=True)
    location = fields.Many2one(comodel_name='stock.location', string='Location', copy=True, store=True)
    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)
