from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    bridge_transfer_location_id = fields.Many2one(comodel_name='stock.location', string='Bridge Transfer Location', copy=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    notification_user_id = fields.Many2one(comodel_name='res.users', string='Notification User', copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, store=True)
