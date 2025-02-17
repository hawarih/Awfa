from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    can_be_rented = fields.Boolean(string='Can be Rented', copy=True, related='product_tmpl_id.can_be_rented')
    rental_additional_service = fields.Many2one(comodel_name='rental.additional.service', string='Additional Service', copy=True, related='product_tmpl_id.rental_additional_service')
    rental_product_type = fields.Selection(string='Rental Product Type', selection=[], copy=True, related='product_tmpl_id.rental_product_type')
