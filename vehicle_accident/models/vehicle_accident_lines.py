from odoo import api, fields, models


class VehicleAccidentLines(models.Model):
    _name = 'vehicle.accident.lines'
    _description = 'Vehicle Accident Lines'

    amount = fields.Float(string='Amount', copy=True, store=True)
    discount_amount = fields.Float(string='Discount Amount', copy=True, store=True)
    is_1st_create_invoice = fields.Boolean(string='Is 1St Create Invoice', readonly=True)
    is_3rd_line = fields.Boolean(string='Is 3rd', copy=True, store=True)
    is_added_to_rental_contract = fields.Boolean(string='Is Added To Rental Contract', copy=True, store=True)
    is_first_line = fields.Boolean(string='Is first', copy=True, store=True)
    item = fields.Many2one(comodel_name='product.product', string='Item', copy=True, store=True)
    net_amount = fields.Float(string='Net Amount Without Taxes', readonly=True)
    net_amount_taxed = fields.Float(string='Net Amount With Taxes', readonly=True)
    remaining = fields.Float(string='Remaining', readonly=True)
    remaining_customer = fields.Many2one(comodel_name='res.partner', string='Remaining Customer', copy=True, store=True)
    taxes = fields.Many2many(comodel_name='account.tax', string='Taxes', help="""Default taxes used when selling the product.""", related='item.taxes_id', readonly=True)
    to_invoice = fields.Float(string='To invoice', copy=True, store=True)
    vehicle_accident_id = fields.Many2one(comodel_name='vehicle.accident', string='Vehicle Accident', copy=True, store=True)

    def second_create_invoice(self):
        pass

    def third_create_invoice(self):
        pass