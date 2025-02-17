from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    parent_category_id = fields.Many2one(comodel_name='product.category', string='Parent Category', related='categ_id.parent_id', readonly=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, readonly=True, store=True)

    _sql_constraints = [
        ('product_template_unique_default_code', 'unique(default_code)', 'Default Code must be unique'),
    ]