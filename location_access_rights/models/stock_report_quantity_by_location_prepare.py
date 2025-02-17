from odoo import api, fields, models


class StockReportQuantityByLocationPrepare(models.TransientModel):
    _inherit = 'stock.report.quantity.by.location.prepare'

    user_location_ids = fields.Many2many(comodel_name='stock.location', string='User Location', 
                                            relation="stock_location_rel", readonly=True)
