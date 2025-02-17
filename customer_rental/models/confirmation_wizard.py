from odoo import api, fields, models


class ConfirmationWizard(models.TransientModel):
    _name = 'confirmation.wizard'
    _description = 'Confirmation Wizard'

    contract_id = fields.Many2one(comodel_name='rental.contract', string='Contract', copy=True, store=True)
    type = fields.Char(string='Type', copy=True, store=True)

    def confirm(self):
        pass