from odoo import api, fields, models


class VehicleChecklist(models.Model):
    _name = 'vehicle.checklist'
    _description = 'Vehicle Checklist'

    ac = fields.Selection(string='Ac', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    car_seats = fields.Selection(string='Car Seats', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    fire_extinguisher = fields.Selection(string='Fire Extinguisher', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit = fields.Selection(string='First Aid Kit', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    fuel_type_code = fields.Selection(string='Fuel Type Code', selection=[('1', '91'), ('2', '95'), ('3', 'Diesel'), ('4', 'Electrical')], copy=True, store=True)
    keys = fields.Selection(string='Keys', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    number_of_keys = fields.Char(string='Number Of Keys', copy=True, store=True)
    oil_change_date = fields.Date(string='Oil Change Date', copy=True, store=True)
    oil_change_km_distance = fields.Float(string='Oil Change Km Distance', copy=True, store=True)
    oil_type_id = fields.Many2one(comodel_name='product.template', string='Oil Type', copy=True, store=True)
    picking_code = fields.Selection(string='Type of Operation', selection=[], related='stock_move_id.picking_id.picking_type_id.code', readonly=True)
    plate_type = fields.Selection(string='Plate Type', selection=[('1', 'Private'), ('3', 'Private Transport')], copy=True, store=True)
    radio_stereo = fields.Selection(string='Radio Stereo', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    safety_triangle = fields.Selection(string='Safety Triangle', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    screen = fields.Selection(string='Screen', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    spare_tire_tools = fields.Selection(string='Spare Tire Tools', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tires = fields.Selection(string='Spare Tires', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    speedometer = fields.Selection(string='Speedometer', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    stock_move_id = fields.Many2one(comodel_name='stock.move', string='Stock Move', copy=True, store=True)
    tires = fields.Selection(string='Tires', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    user_id = fields.Many2one(comodel_name='res.users', string='User', copy=True, readonly=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, readonly=True, store=True)
    vehicle_status = fields.Selection(string='Vehicle Status', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, store=True)

    def action_check(self):
        pass