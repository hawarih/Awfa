from odoo import api, fields, models


class CardVehicleHistory(models.Model):
    _name = 'card.vehicle.history'
    _description = 'Card Vehicle History'

    card_id = fields.Many2one(comodel_name='fleet.card', string='Card', copy=True, ondelete='set null', store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    gps_id = fields.Many2one(comodel_name='gps.gps', string='GPS', copy=True, ondelete='set null', store=True)
    state = fields.Selection(string='State', selection=[('assigned', 'Assigned'), ('unassigned', 'Unassigned')], store=True)
    user_id = fields.Many2one(comodel_name='res.users', string='User', copy=True, ondelete='set null', store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, ondelete='set null', store=True)
