from odoo import api, fields, models


class ViewNaqlContractWizard(models.TransientModel):
    _name = 'view.naql.contract.wizard'
    _description = 'View Naql Contract Wizard'

    contract_json = fields.Text(string='Contract Json', copy=True, store=True)
    contract_pdf = fields.Binary(string='Contract Pdf', copy=True, store=True)
    file_name = fields.Char(string='File Name', copy=True, store=True)
    request_type = fields.Selection(string='Request Type', selection=[('summarized_pdf', 'Summarized PDF'), ('full_pdf', 'Full PDF'), ('json', 'Contract Json')], copy=True, required=True, store=True)

    def action_apply(self):
        pass