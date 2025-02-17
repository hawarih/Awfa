from odoo import api, fields, models


class VehicleData(models.TransientModel):
    _name = 'vehicle.data'
    _description = 'Vehicle Data'

    license_plate = fields.Char(string='Plate Number', copy=True, store=True)
    model_id = fields.Many2one(comodel_name='fleet.vehicle.model', string='Model', copy=True, ondelete='set null', store=True)
    net_car_value = fields.Float(string='Purchase Price', copy=True, store=True)
    quantity = fields.Integer(string='Quantity', copy=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='create.vehicle.wizard', string='Vehicle', copy=True, ondelete='set null', store=True)
