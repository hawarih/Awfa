from odoo import api, fields, models
from odoo.exceptions import UserError

class CustomerRentalPolicy(models.Model):
    _name = 'customer.rental.policy'
    _description = 'Customer Rental Policy'

    after = fields.Text(string='After', copy=True, store=True)
    before = fields.Text(string='Before', copy=True, store=True)
    name = fields.Selection(string='Name', selection=[('actual', 'Actual'), ('full', 'Full')], copy=True, required=True, store=True)
    on_time = fields.Text(string='On Time', copy=True, store=True)
    related_plan = fields.Many2many(comodel_name='customer.rental.plan', string='Related Plan', copy=True, relation='customer_rental_plan_customer_rental_policy_rel', column1='customer_rental_policy_id', column2='customer_rental_plan_id', store=True)


    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'This name already created.'),
    ]
    
    
    def remove_pricing_line(self, pricing_line_type, removed_plan_ids):
        line_to_delete = pricing_line_type.filtered(lambda line: line.plan_id.id in removed_plan_ids)
        if line_to_delete:
            line_to_delete.unlink()
            
    def create_pricing_line(self, pricing, rental_price_type, added_plan_ids):
        pricing_lines = self.env['customer.rental.pricing.lines']
        for plan in added_plan_ids:
            pricing_lines.create({'plan_id': plan, 'price': 0, rental_price_type: pricing.id})
    
    def write(self, values):
        old_plan_ids = set(self.related_plan.ids)
        res = super().write(values)
        new_plan_ids = set(self.related_plan.ids)
        
        if values.get('related_plan'):
            pricings = self.env['customer.rental.pricing'].search([])
            
            if len(old_plan_ids) > len(new_plan_ids):
                removed_plan_ids = old_plan_ids - new_plan_ids
                if self.name == 'actual':
                    for pricing in pricings:
                        self.remove_pricing_line(pricing.actual_pricing_lines, removed_plan_ids)
                if self.name == 'full':
                    for pricing in pricings:
                        self.remove_pricing_line(pricing.full_pricing_lines, removed_plan_ids)

                            
            if len(old_plan_ids) < len(new_plan_ids):
                added_plan_ids = new_plan_ids - old_plan_ids
                if self.name == 'actual':
                    for pricing in pricings:
                        self.create_pricing_line(pricing, 'rental_price_id_actual', added_plan_ids)
                    
                if self.name == 'full':
                    for pricing in pricings:
                        self.create_pricing_line(pricing, 'rental_price_id_full', added_plan_ids)

        return res