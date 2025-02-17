from odoo import api, fields, models


class CustomerRentalSetting(models.Model):
    _name = 'customer.rental.setting'
    _description = 'Customer Rental Setting'

    name = fields.Char(string='Name', copy=True, store=True)
