from odoo import api, fields, models


class CustomerRentalReturnWizard(models.TransientModel):
    _inherit = 'customer.rental.return.wizard'

    user_allowed_location_ids = fields.Many2many(comodel_name='stock.location', string='User Allowed Location', readonly=True)
