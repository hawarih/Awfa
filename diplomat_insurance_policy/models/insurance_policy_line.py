from odoo import api, fields, models


class InsurancePolicyLine(models.Model):
    _name = 'insurance.policy.line'
    _description = 'Insurance Policy Line'

    card_number = fields.Char(string='Card Number', copy=True, store=True)
    chasis_num = fields.Char(string='Chasis Number', copy=True, store=True)
    days = fields.Integer(string='Days', readonly=True)
    end_date = fields.Date(string='End Date', copy=True, store=True)
    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, readonly=True, ondelete='cascade', store=True)
    invoiced = fields.Boolean(string='Invoiced', copy=True, readonly=True, store=True)
    license_plate = fields.Char(string='License Plate', copy=True, store=True)
    price_unit = fields.Float(string='Price Unit', copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', related='vehicle_id.product_id', readonly=True)
    qty = fields.Float(string='Quantity', copy=True, store=True)
    start_date = fields.Date(string='Start Date', copy=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('run', 'Running'), ('stop', 'Stopped')], 
                                                default='draft', readonly=True, store=True)
    subtotal = fields.Float(string='SubTotal', readonly=True, store=True)
    tax_amount = fields.Float(string='Taxes Amount', readonly=True)
    taxes_id = fields.Many2many(comodel_name='account.tax', string='Taxes', copy=True, relation='account_tax_insurance_policy_line_rel', column1='insurance_policy_line_id', column2='account_tax_id', store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, readonly=True, ondelete='cascade', store=True)

    def action_stop(self):
        pass