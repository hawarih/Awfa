from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    payment_revenue_type = fields.Selection(string='Payment Revenue Type', selection=[('rental', 'Rental Income'), ('compensation', 'Compensation Income'), ('other', 'Other Income'), ('car_sale', 'Car Sale Income'), ('supply', 'Supply Income')], copy=True, store=True)
