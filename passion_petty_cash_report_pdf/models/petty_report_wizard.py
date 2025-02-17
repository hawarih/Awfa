from odoo import api, fields, models


class PettyReportWizard(models.TransientModel):
    _name = 'petty.report.wizard'
    _description = 'Petty Report Wizard'

    date_from = fields.Date(string='Date From', copy=True, store=True)
    date_to = fields.Date(string='Date To', copy=True, store=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', copy=True, required=True, ondelete='cascade', store=True)

    def action_print(self):
        pass
