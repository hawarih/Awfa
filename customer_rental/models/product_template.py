from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    can_be_rented = fields.Boolean(string='Can be Rented', copy=True, store=True)
    rental_additional_service = fields.Many2one(comodel_name='rental.additional.service', string='Additional Service', copy=True, store=True)
    rental_product_type = fields.Selection(string='Rental Product Type', selection=[('is_trip', 'Is Trip'), ('is_external_authorization', 'Is External Authorization'), ('is_internal_authorization', 'Is Internal Authorization'), ('accident_cost', 'Accident Cost'), ('is_KM_extra', 'Is KM Extra'), ('is_additional_service', 'Is Additional Service'), ('is_fuel_cost', 'Fuel Cost'), ('damages', 'Damages'), ('is_discount', 'Discount'), ('is_extra', 'Extra'), ('already_invoiced', 'Already Invoiced'), ('charged_late_hours', 'Charged Late Hours'), ('early_hours', 'Early Hours'), ('extra_hours', 'Extra Hours'), ('additional_services_extra', 'Additional Services Extra'), ('reconciled_trip_days', 'Reconciled Trip Days'), ('late_hours_cost', 'Late Hours Cost'), ('opened_contract_penalty', 'Opened Contract Penalty')], copy=True, store=True)
