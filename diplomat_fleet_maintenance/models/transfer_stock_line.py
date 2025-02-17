from odoo import api, fields, models


class TransferStockLine(models.TransientModel):
    _name = 'transfer.stock.line'
    _description = 'Transfer Stock Line'

    ac_out = fields.Selection(string='Ac Out', selection=[], related='maintenance_id.ac_in')
    car_seats_out = fields.Selection(string='Car Seats Out', selection=[], related='maintenance_id.car_seats_in')
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True,  store=True)
    destination = fields.Text(string='Destination', copy=True, store=True)
    driver_id = fields.Many2one(comodel_name='vehicle.driver', string='Driver', copy=True,  store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True,  store=True)
    fire_extinguisher_out = fields.Selection(string='Fire Extinguisher Out', selection=[], related='maintenance_id.fire_extinguisher_in')
    first_aid_kit_out = fields.Selection(string='First Aid Kit Out', selection=[], related='maintenance_id.first_aid_kit_in')
    from_warehouse_id = fields.Many2one(comodel_name='stock.warehouse', string='From Warehouse', related='maintenance_id.maintenance_team_id.picking_type_id.warehouse_id', readonly=True)
    keys_out = fields.Selection(string='Keys Out', selection=[], related='maintenance_id.keys_in')
    maintenance_id = fields.Many2one(comodel_name='maintenance.request', string='Maintenance', copy=True,  store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', related='vehicle_id.product_id', readonly=True)
    radio_stereo_out = fields.Selection(string='Radio Stereo Out', selection=[], related='maintenance_id.radio_stereo_in')
    safety_triangle_out = fields.Selection(string='Safety Triangle Out', selection=[], related='maintenance_id.safety_triangle_in')
    screen_out = fields.Selection(string='Screen Out', selection=[], related='maintenance_id.screen_in')
    spare_tire_tools_out = fields.Selection(string='Spare Tire Tools Out', selection=[], related='maintenance_id.spare_tire_tools_in')
    spare_tires_out = fields.Selection(string='Spare Tires Out', selection=[], related='maintenance_id.spare_tires_in')
    speedometer_out = fields.Selection(string='Speedometer Out', selection=[], related='maintenance_id.speedometer_in')
    tires_out = fields.Selection(string='Tires Out', selection=[], related='maintenance_id.tires_in')
    transfer_type = fields.Selection(string='Transfer Type', selection=[('external', 'External'), ('internal', 'Internal'), ('custody', 'Custody'), ('task', 'Task'), ('return', 'Return'), ('maintenance', 'Maintenance')], copy=True, readonly=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True,  store=True)
    vehicle_status_out = fields.Selection(string='Vehicle Status Out', selection=[], related='maintenance_id.vehicle_status_in')

    def create_internal_stock_transfer(self):
        pass
