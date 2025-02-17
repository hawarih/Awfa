from odoo import api, fields, models


class RentalContractLines(models.Model):
    _name = 'rental.contract.lines'
    _description = 'Rental Contract Lines'

    contract_id = fields.Many2one(comodel_name='rental.contract', string='Contract', copy=True, store=True)
    count = fields.Integer(string='Count', copy=True, store=True)
    discount_amount = fields.Float(string='Discount Amount', copy=True, store=True)
    has_allow_edit_trip_days_group = fields.Boolean(string='Has Allow Edit Trip Days Group', readonly=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, store=True)
    rental_product_type = fields.Selection(string='Rental Product Type', selection=[], related='product_id.rental_product_type', readonly=True)
    subtotal_with_tax = fields.Float(string='Subtotal with tax', readonly=True)
    subtotal_without_tax = fields.Float(string='Subtotal', readonly=True)
    taxes_id = fields.Many2many(comodel_name='account.tax', string='Taxes', copy=True, relation='account_tax_rental_contract_lines_rel', column1='rental_contract_lines_id', column2='account_tax_id', store=True)
    unit_of_measure = fields.Many2one(comodel_name='uom.uom', string='UoM', copy=True, store=True)
    unit_price = fields.Float(string='Unit Price', copy=True, store=True)
