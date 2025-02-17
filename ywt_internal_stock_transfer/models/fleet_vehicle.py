from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    ac_in = fields.Selection(string='Ac In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    car_seats_in = fields.Selection(string='Car Seats In', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    fire_extinguisher_in = fields.Selection(string='Fire Extinguisher In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit_in = fields.Selection(string='First Aid Kit In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    keys_in = fields.Selection(string='Keys In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    plate_type_in = fields.Selection(string='Plate Type In', selection=[('1', 'Private'), ('3', 'Private Transport')], copy=True, store=True)
    radio_stereo_in = fields.Selection(string='Radio Stereo In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    safety_triangle_in = fields.Selection(string='Safety Triangle In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    screen_in = fields.Selection(string='Screen In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    spare_tire_tools_in = fields.Selection(string='Spare Tire Tools In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tires_in = fields.Selection(string='Spare Tires In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    speedometer_in = fields.Selection(string='Speedometer In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    state_old = fields.Many2one(comodel_name='fleet.vehicle.state', string='State Old', copy=True, store=True)
    tires_in = fields.Selection(string='Tires In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    vehicle_status_in = fields.Selection(string='Vehicle Status In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, store=True)
