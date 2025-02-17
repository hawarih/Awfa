from odoo import api, fields, models


class ProductCardReportWizard(models.TransientModel):
    _name = 'product.card.report.wizard'
    _description = 'Product Card Report Wizard'

    allowed_location_card_ids = fields.Many2many(comodel_name='stock.location', string='Allowed Location Card', copy=True, relation='allowed_location_card_ids_rel', column1='product_card_report_wizard_id', column2='stock_location_id', store=True)
    date_from = fields.Datetime(string='Date From', copy=True, store=True)
    date_to = fields.Datetime(string='Date To', copy=True, store=True)
    default_code = fields.Char(string='Default Code', copy=True, store=True)
    excel_sheet = fields.Binary(string='Excel Sheet', copy=True, store=True)
    excel_sheet_name = fields.Char(string='Excel Sheet Name', copy=True, store=True)
    location_id = fields.Many2many(comodel_name='stock.location', string='Location', copy=True, relation='product_card_report_wizard_stock_location_rel', column1='product_card_report_wizard_id', column2='stock_location_id', store=True)
    name = fields.Char(string='Name', copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True,  store=True)
    product_tmpl_id = fields.Many2one(comodel_name='product.template', string='Product Tmpl', copy=True,  store=True)
    report_type = fields.Selection(string='Status', selection=[('xls', 'XLS'), ('html', 'HTML')], copy=True, required=True, store=True)

    def action_print(self):
        pass
