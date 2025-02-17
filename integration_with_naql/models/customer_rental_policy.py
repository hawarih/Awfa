from odoo import api, fields, models


class CustomerRentalPolicy(models.Model):
    _inherit = 'customer.rental.policy'

    naql_policy = fields.Integer(string='Naql Policy  ID', copy=True, store=True)
