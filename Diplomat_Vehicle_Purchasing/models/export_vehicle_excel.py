from odoo import api, fields, models


class ExportVehicleExcel(models.TransientModel):
    _name = 'export.vehicle.excel'
    _description = 'Export Vehicle Excel'

    excel_file = fields.Binary(string='Purchase Vehicle Excel Report', copy=True, readonly=True, store=True)
    file_name = fields.Char(string='Excel File', copy=True, readonly=True, size=64, store=True)
