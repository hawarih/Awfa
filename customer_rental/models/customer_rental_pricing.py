from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class CustomerRentalPricing(models.Model):
    _name = 'customer.rental.pricing'
    _description = 'Customer Rental Pricing'

    actual_pricing_lines = fields.One2many(comodel_name='customer.rental.pricing.lines', inverse_name='rental_price_id_actual', string='Actual Pricing Lines', store=True)
    allowed_hours = fields.Float(string='Allowed Hours', copy=True, store=True)
    date_from = fields.Date(string='From', copy=True, store=True)
    date_to = fields.Date(string='To', copy=True, store=True)
    fuel = fields.Float(string='Fuel', copy=True, store=True)
    full_pricing_lines = fields.One2many(comodel_name='customer.rental.pricing.lines', inverse_name='rental_price_id_full', string='Full Pricing Lines', store=True)
    km_extra_cost = fields.Float(string='Km Extra Cost', copy=True, store=True)
    km_free = fields.Float(string='Km Free', copy=True, store=True)
    km_open_percentage = fields.Integer(string='Km Open Percentage', copy=True, store=True)
    location = fields.Many2many(comodel_name='stock.location', string='Location', copy=True, relation='customer_rental_pricing_stock_location_rel', column1='customer_rental_pricing_id', column2='stock_location_id', store=True)
    models = fields.Many2many(comodel_name='fleet.vehicle.model', string='Models', copy=True, required=True, relation='customer_rental_pricing_fleet_vehicle_model_rel', column1='customer_rental_pricing_id', column2='fleet_vehicle_model_id', store=True)
    name = fields.Text(string='Name', copy=True, required=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('confirmed', 'Confirmed'), ('archived', 'Archived')], default='draft', store=True)


    def _check_unique_models(self):
        for record in self:
            if record.models:
                # Search for other records with overlapping models
                conflicting_records = self.search([
                    ('id', '!=', record.id),  # Exclude the current record
                    ('models', 'in', record.models.ids),  # Check for models overlap
                ])
                if conflicting_records:
                    raise UserError("There exist a model that already exists in another rental pricing record,Or the current rental pricing field ( Date From ) is overlapping another .")
        
    def _create_policy_lines(self):
        actual_pricing_record = self.env['customer.rental.policy'].search([('name', '=', 'actual')])
        policy_line = []
        for policy in actual_pricing_record.related_plan:
            policy_plan_vals = {
                'plan_id': policy.id,
                'price': 0,
            }
            policy_line.append((0, 0, policy_plan_vals))
        self.actual_pricing_lines = policy_line
            
        full_pricing_record = self.env['customer.rental.policy'].search([('name', '=', 'full')])
        policy_line.clear()
        for policy in full_pricing_record.related_plan:
            policy_plan_vals = {
                'plan_id': policy.id,
                'price': 0,
            }
            policy_line.append((0, 0, policy_plan_vals))
        self.full_pricing_lines = policy_line
    
    @api.model
    def create(self, vals_list):
        res = super(CustomerRentalPricing, self).create(vals_list)
        km_free = vals_list.get('km_free')
        km_extra_cost = vals_list.get('km_extra_cost')
        fuel = vals_list.get('fuel')
        
        if self.raise_error_for_km_cost_fuel(km_free, km_extra_cost, fuel, creating=True):
            raise ValidationError("The value of KM Free, KM Free Cost, Fuel must be greater than or equal to 0.")
        res._check_unique_models()
        
        res._create_policy_lines()
        return res
    
    def write(self, vals):
        km_free = vals.get('km_free')
        km_extra_cost = vals.get('km_extra_cost')
        fuel = vals.get('fuel')
        
        print(km_free, km_extra_cost, fuel)
        
        if self.raise_error_for_km_cost_fuel(km_free, km_extra_cost, fuel):
            raise ValidationError("The value of KM Free, KM Free Cost, Fuel must be greater than or equal to 0.")
        
        if vals.get('models'):
            self._check_unique_models()
        return super().write(vals)

    def raise_error_for_km_cost_fuel(self, km_free, km_extra_cost, fuel, creating=False):
        raise_error = False
        if creating:
            if not km_free or km_free <= 0:
                raise_error = True
            if not km_extra_cost or km_extra_cost <= 0:
                raise_error = True
            if not fuel or fuel <= 0:
                raise_error = True
        else:
            if km_free != None:
                if km_free: 
                    if km_free <= 0:
                        raise_error = True
            if km_extra_cost != None:
                if km_extra_cost: 
                    if km_extra_cost <= 0:
                        raise_error = True
            if fuel != None:
                if fuel: 
                    if fuel <= 0:
                        raise_error = True
        return raise_error
             