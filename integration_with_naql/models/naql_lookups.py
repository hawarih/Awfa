from odoo import api, fields, models


class NaqlLookups(models.TransientModel):
    _name = 'naql.lookups'
    _description = 'Naql Lookups'

    data = fields.Html(string='Data', copy=True, store=True)
    request_type = fields.Selection(string='Request Type', selection=[('authorization-type', 'Authorization Type'), ('contract-status', 'Contract Status'), ('contract-type', 'Contract Type'), ('external-authorization-countries', 'External Authorization Countries'), ('fuel-type', 'Fuel Type'), ('id-type', 'ID Type'), ('payment-method', 'Payment Method'), ('yakeen-nationality', 'Yakeen Nationality'), ('gccNationality', 'GCC Nationality'), ('country', 'Country'), ('closure-reasons', 'Closure Reasons'), ('suspension-reasons', 'Suspension Reasons')], copy=True, required=True, store=True)

    def get_contract(self):
        pass