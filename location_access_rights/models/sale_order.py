from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    user_location_ids = fields.Many2many(comodel_name='stock.location', string='User Location', copy=True, relation='allowed_user3_location3_rel', column1='allowed_location_id3', column2='allowed_user_id3', store=True)
