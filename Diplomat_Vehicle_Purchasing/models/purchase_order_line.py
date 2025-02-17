from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    admin_fee = fields.Float(string='Adminstrative Fee', copy=True, store=True)
    insurance = fields.Float(string='Insurance', copy=True, store=True)
    interest = fields.Float(string='Interest', readonly=True)
    license_plate = fields.Char(string='Plate Number', help="""License plate number of the vehicle (i = plate number for a car)""", related='vehicle_id.license_plate', readonly=True)
    model_id = fields.Many2one(comodel_name='fleet.vehicle.model', string='Model', related='vehicle_id.model_id', readonly=True, store=True)
    owner_ship = fields.Float(string='Ownership Value', copy=True, store=True)
    plates_fee = fields.Float(string='Plates Fees', copy=True, store=True)
    product_ids = fields.Many2many(comodel_name='product.product', string='products', readonly=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', related='product_id.vehicle_id', readonly=True)

    def delete_vehicle(self):
        pass
