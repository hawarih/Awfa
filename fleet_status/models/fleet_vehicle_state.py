from odoo import api, fields, models


class FleetVehicleState(models.Model):
    _inherit = 'fleet.vehicle.state'

    type = fields.Selection(string='Type', selection=[('ready_rent', 'Ready to Rent'), ('ready_sell', 'Ready to Sell'), ('reserved', 'Reserved'), 
                                                      ('new_car', 'New Car'), ('under_preparing', 'Under Preparing'), ('out_service', 'Out of Service'), 
                                                      ('sold', 'Sold'), ('stolen', 'Stolen'), ('by_reservation', 'By Reservation'), ('movable', 'Movable'), 
                                                      ('shipping', 'Shipping'), ('custody_employee', 'Custody of an employee'), ('job_assignment', 'Job Assignment'), 
                                                      ('maintenance', 'Maintenance'), ('accident', 'Accident'), ('rented', 'Rented'), ('recovery', 'Recovery'), 
                                                      ('non_existent', 'Non-existent')], 
                                            copy=True, store=True)
