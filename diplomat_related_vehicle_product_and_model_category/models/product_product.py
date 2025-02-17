from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    parent_category_id = fields.Many2one(comodel_name='product.category', string='Parent Category', related='product_tmpl_id.parent_category_id', readonly=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, related='product_tmpl_id.vehicle_id', readonly=True)

    def name_get(self):
        result = []
        for product in self:
            name = product.name
            result.append((product.id, name))
        return result