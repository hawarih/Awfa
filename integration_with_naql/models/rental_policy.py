from odoo import api, fields, models


class RentalPolicy(models.Model):
    _name = 'rental.policy'
    _description = 'Rental Policy'

    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    naql_policy = fields.Integer(string='Naql Policy  ID', copy=True, store=True)


    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Name must be unique')
    ]