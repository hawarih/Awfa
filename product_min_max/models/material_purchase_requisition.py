from odoo import api, fields, models


class MaterialPurchaseRequisition(models.Model):
    _inherit = 'material.purchase.requisition'

    destination_location_id = fields.Many2one(comodel_name='stock.location', string='Default Destination Location', help="""This is the default destination location when you create a picking manually with this operation type. It is possible however to change it or that the routes put another location. If it is empty, it will check for the customer location on the partner. """, related='custom_picking_type_id.default_location_dest_id', readonly=True)
    source_location_id = fields.Many2one(comodel_name='stock.location', string='Default Source Location', help="""This is the default source location when you create a picking manually with this operation type. It is possible however to change it or that the routes put another location. If it is empty, it will check for the supplier location on the partner. """, related='custom_picking_type_id.default_location_src_id', readonly=True)

    def force_confirm(self):
        pass