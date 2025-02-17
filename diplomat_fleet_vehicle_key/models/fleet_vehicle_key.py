from odoo import api, fields, models


class FleetVehicleKey(models.Model):
    _name = 'fleet.vehicle.key'
    _description = 'Fleet Vehicle Key'

    department_id = fields.Many2one(comodel_name='hr.department', string='Department', copy=True,  store=True)
    list_price = fields.Float(string='Sales Price', help="""Price at which the product is sold to customers.""", related='product_id.list_price', readonly=True)
    location_id = fields.Many2one(comodel_name='stock.location', string='Location', copy=True,  store=True)
    lot_id = fields.Many2one(comodel_name='stock.lot', string='Serial number', copy=True, required=True, ondelete='restrict', store=True, tracking=100)
    lot_ids = fields.Many2many(comodel_name='stock.lot', string='Lot', readonly=True)
    name = fields.Char(string='Name', readonly=True, store=True)
    product_id = fields.Many2one(comodel_name='product.template', string='Related Product', copy=True,  store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('available', 'Available'), ('not_available', 'Not Available')], default='draft', store=True)
    type = fields.Selection(string='Key Type', selection=[], related='product_id.key_type', readonly=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Assign Vehicle', copy=True,  store=True)

    def action_confirm(self):
        pass

    def reset_to_draft(self):
        pass

    def action_scrap_key(self):
        pass

    def action_view_scrap_ids(self):
        pass
