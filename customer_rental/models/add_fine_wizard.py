from odoo import api, fields, models


class AddFineWizard(models.TransientModel):
    _name = 'add.fine.wizard'
    _description = 'Add Fine Wizard'

    customer_tax = fields.Many2many(comodel_name='account.tax', string='Customer Taxes', help="""Default taxes used when selling the product.""", related='product_id.taxes_id', readonly=True)
    description = fields.Text(string='Description', copy=True, required=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='product', copy=True, store=True)
    quantity = fields.Integer(string='Quantity', copy=True, readonly=True, store=True)
    unit_of_measure = fields.Many2one(comodel_name='uom.uom', string='UoM', help="""Default unit of measure used for all stock operations.""", related='product_id.uom_id', readonly=True)
    unit_price = fields.Float(string='Unit Price', help="""Price at which the product is sold to customers.""", related='product_id.list_price')

    def save_button(self):
        pass