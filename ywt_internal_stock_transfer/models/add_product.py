from odoo import api, fields, models


class AddProduct(models.TransientModel):
    _name = 'add.product'
    _description = 'Add Product'

    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, required=True, ondelete='cascade', store=True)
    product_ids = fields.Many2many(comodel_name='product.product', string='Product', readonly=True)

    def add_vehicle(self):
        pass
