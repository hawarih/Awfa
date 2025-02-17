from odoo import api, fields, models


class CustomerRentalPricingLines(models.Model):
    _name = 'customer.rental.pricing.lines'
    _description = 'Customer Rental Pricing Lines'

    plan_id = fields.Many2one(comodel_name='customer.rental.plan', string='Plan', copy=True, store=True)
    plan_name = fields.Selection(string='Name', selection=[], related='plan_id.name', readonly=True)
    price = fields.Float(string='Price', copy=True, required=True, store=True)
    rental_price_id_actual = fields.Many2one(comodel_name='customer.rental.pricing', string='Rental Price Id Actual', copy=True, store=True)
    rental_price_id_full = fields.Many2one(comodel_name='customer.rental.pricing', string='Rental Price Id Full', copy=True, store=True)
