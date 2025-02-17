from odoo import api, fields, models


class GpsGps(models.Model):
    _inherit = 'gps.gps'
        
    card_ids = fields.One2many(comodel_name='fleet.card', inverse_name='gps_id', string='Card', readonly=True, store=True)
    card_lot_id = fields.Many2one(comodel_name='stock.lot', string='Card Serial Number', readonly=True, ondelete='set null')
    card_lot_id_store = fields.Many2one(comodel_name='stock.lot', string='Card Serial Number', related='card_lot_id', readonly=True, store=True)
