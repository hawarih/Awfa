from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    color_in_side = fields.Selection(string='Color in side', selection=[('white', 'white'), ('light_blue', 'light_blue'), ('blue', 'blue'), ('black', 'black'), ('red', 'red'), ('blue_white', 'blue_white'), ('dark_blue', 'dark_blue'), ('black_and_white', 'black_and_white'), ('grey', 'grey'), ('light_grey', 'light_grey'), ('light_brown', 'light_brown'), ('brown', 'brown'), ('dark_grey', 'dark_grey'), ('beige', 'beige'), ('silver', 'silver'), ('green', 'green'), ('blue_and_white', 'blue_and_white')], copy=True, store=True)
    engine_capacity = fields.Char(string='Engine Capacity', copy=True, store=True)
    gps_name = fields.Char(string='GPS name', copy=True, readonly=True, store=True)
    gps_status = fields.Selection(string='GPS Status', selection=[('working', 'Working'), ('not working', 'Not Working')], copy=True, readonly=True, store=True)
    owner_hip_type = fields.Selection(string='Owner Ship Type', selection=[('diplomat', 'Diplomat'), ('borrowed', 'Borrowed'), ('sponsored', 'Sponsored')], copy=True, store=True)
    owner_id_no = fields.Char(string='Owner ID number', readonly=True)
    owner_name = fields.Char(string='Owner Name', related='vendor_id.name', readonly=True)
    related_product = fields.Many2one(comodel_name='product.template', string='Related Product', copy=True, readonly=True, store=True)
    seats = fields.Integer(string='Seats Number', help="""Number of seats of the vehicle""", related='model_id.seats', readonly=True, store=True)
    serial_no = fields.Many2one(comodel_name='stock.lot', string='Serial Number', copy=True, readonly=True, store=True)
    transmission_type = fields.Selection(string='Transmission Type', selection=[], related='model_id.transmission', readonly=True)
