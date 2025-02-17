from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'
        
    card_name = fields.Char(string='Card name', related='gps_id.card_ids.name', readonly=True, store=True, )
    card_related_product = fields.Many2one(comodel_name='product.template', string='Related Product', related='gps_id.card_ids.related_product', readonly=True, )
    card_serial_no = fields.Many2one(comodel_name='stock.lot', string='Serial Number', related='gps_id.card_ids.lot_id', readonly=True, )
    card_status = fields.Selection(string='Card Status', selection=[], related='gps_id.card_ids.state', readonly=True, )
    gps_id = fields.Many2one(comodel_name='gps.gps', string='Gps', readonly=True, ondelete='set null')


    def card_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Card History',
            'res_model': 'card.vehicle.history',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'target': 'current',
        }
