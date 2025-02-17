from odoo import api, fields, models


class VehicleNaqlContractWizard(models.TransientModel):
    _name = 'vehicle.naql.contract.wizard'
    _description = 'Vehicle Naql Contract Wizard'

    contract_json = fields.Text(string='Contract Json', copy=True, readonly=True, store=True)
