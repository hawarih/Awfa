from odoo import api, fields, models


class GetData(models.TransientModel):
    _name = 'get.data'
    _description = 'Get Data'

    data = fields.Html(string='Data', copy=True, store=True)
    request_type = fields.Selection(string='Request Type', selection=[('branch', 'Branch'), ('policy', 'Policy'), ('extended_coverage', 'Extended Coverage')], copy=True, required=True, store=True)

    def get_contract(self):
        pass