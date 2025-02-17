from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    license_plate = fields.Char(string='Plate Number', help="""License plate number of the vehicle (i = plate number for a car)""", related='vehicle_id.license_plate', readonly=True)
    model_id = fields.Many2one(comodel_name='fleet.vehicle.model', string='Model', related='vehicle_id.model_id', readonly=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', related='product_id.vehicle_id', readonly=True)
    vin_sn = fields.Char(string='Chassis Number', help="""Unique number written on the vehicle motor (VIN/SN number)""", related='vehicle_id.vin_sn', readonly=True)
