from odoo import api, fields, models


class StockInventoryLine(models.Model):
    _name = 'stock.inventory.line'
    _description = 'Stock Inventory Line'

    actual_cost = fields.Float(string='Actual Cost', copy=True, store=True)
    categ_id = fields.Many2one(comodel_name='product.category', string='Product Category', related='product_id.categ_id', readonly=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', related='inventory_id.company_id', readonly=True, index=True, store=True)
    difference_qty = fields.Float(string='Difference', help="""Indicates the gap between the product's theoretical quantity and its newest quantity.""", readonly=True)
    inventory_date = fields.Datetime(string='Inventory Date', help="""Last date at which the On Hand Quantity has been computed.""", copy=True, readonly=True, store=True)
    inventory_display_name = fields.Char(string='Inventory Reference', related='inventory_id.name', readonly=True)
    inventory_id = fields.Many2one(comodel_name='stock.inventory', string='Inventory', copy=True, index=True, ondelete='cascade', store=True)
    is_editable = fields.Boolean(string='Is Editable', help="""Technical field to restrict editing.""", copy=True, store=True)
    location_id = fields.Many2one(comodel_name='stock.location', string='Location', copy=True, required=True, index=True, ondelete='restrict', store=True)
    outdated = fields.Boolean(string='Quantity outdated', readonly=True)
    package_id = fields.Many2one(comodel_name='stock.quant.package', string='Pack', copy=True, index=True, ondelete='set null', store=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Owner', copy=True, ondelete='set null', store=True)
    prod_lot_id = fields.Many2one(comodel_name='stock.lot', string='Lot/Serial Number', copy=True, ondelete='set null', store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, required=True, index=True, ondelete='restrict', store=True)
    product_qty = fields.Float(string='Counted Quantity', copy=True, readonly=True, store=True)
    product_tracking = fields.Selection(string='Tracking', help="""Ensure the traceability of a storable product in your warehouse.""", selection=[], related='product_id.tracking', readonly=True)
    product_uom_category_id = fields.Many2one(comodel_name='uom.category', string='Category', help="""Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios.""", related='product_id.uom_id.category_id', readonly=True)
    product_uom_id = fields.Many2one(comodel_name='uom.uom', string='Product Unit of Measure', copy=True, required=True, ondelete='restrict', store=True)
    state = fields.Selection(string='Status', selection=[], related='inventory_id.state', readonly=True)
    theoretical_qty = fields.Float(string='Theoretical Quantity', copy=True, readonly=True, store=True)
    total_diff_value = fields.Float(string='Total Diff Value', copy=True, store=True)

    def action_refresh_quantity(self):
        pass