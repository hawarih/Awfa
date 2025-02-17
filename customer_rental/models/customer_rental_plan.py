from odoo import api, fields, models


class CustomerRentalPlan(models.Model):
    _name = 'customer.rental.plan'
    _description = 'Customer Rental Plan'

    name = fields.Selection(string='Name', selection=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('annually', 'annually'), ('motivational', 'Motivational')], copy=True, required=True, store=True)
    related_policy = fields.Many2many(comodel_name='customer.rental.policy', string='Related Policy', copy=True, readonly=True, relation='customer_rental_plan_customer_rental_policy_rel', column1='customer_rental_plan_id', column2='customer_rental_policy_id', store=True)


    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'This name already created.'),
    ]