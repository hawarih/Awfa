from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_location = fields.Many2many(comodel_name='stock.location', string='Allowed Location', copy=True, relation='stock_user_rel', column1='allowed_location_id', column2='allowed_user_id', store=True)
    location_ids = fields.Many2many(comodel_name='stock.location', string='Location', copy=True, relation='res_users_stock_location_rel', column1='res_users_id', column2='stock_location_id', store=True)
    picking_type_ids = fields.Many2many(comodel_name='stock.picking.type', string='Picking Type', copy=True, relation='res_users_stock_picking_type_rel', column1='res_users_id', column2='stock_picking_type_id', store=True)
