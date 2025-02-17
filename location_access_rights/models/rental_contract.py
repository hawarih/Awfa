from odoo import api, fields, models


class RentalContract(models.Model):
    _inherit = 'rental.contract'

    user_allowed_location_ids = fields.Many2many(comodel_name='stock.location', relation="user_allowed_location_rel", string='User Allowed Location', readonly=True,
                                                 default=lambda self: self.env.user.allowed_location)
    user_location_ids = fields.Many2many(comodel_name='stock.location', relation="user_location_rel", string='User Location', readonly=True,
                                        default=lambda self: self.env.user.location_ids)
