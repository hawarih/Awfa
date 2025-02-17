from odoo import api, fields, models


class StockReportQuantityByLocationPrepare(models.TransientModel):
    _name = 'stock.report.quantity.by.location.prepare'
    _description = 'Stock Report Quantity By Location Prepare'

    allowed_location_ids = fields.Many2many(comodel_name='stock.location', string='Allowed Location', copy=True, relation='allowed_location_ids_rel', column1='stock_report_quantity_by_location_prepare_id', column2='stock_location_id', store=True)
    location_ids = fields.Many2many(comodel_name='stock.location', string='Locations', copy=True, required=True, relation='stock_location_stock_report_quantity_by_location_prepare_rel', column1='stock_report_quantity_by_location_prepare_id', column2='stock_location_id', store=True)
    with_quantity = fields.Boolean(string='Quantity > 0', help="""Show only the products that have existing quantity on hand""", copy=True, store=True)

    def open(self):
        pass