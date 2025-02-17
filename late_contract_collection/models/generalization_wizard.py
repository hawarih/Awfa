from odoo import api, fields, models


class GeneralizationWizard(models.TransientModel):
    _name = 'generalization.wizard'
    _description = 'Generalization Wizard'

    contract_id = fields.Many2one(comodel_name='rental.contract', string='Contract', copy=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    follower = fields.Many2one(comodel_name='hr.employee', string='Follower', copy=True, store=True)
    generalization_number = fields.Integer(string='Generalization Number', copy=True, store=True)
    location = fields.Many2one(comodel_name='stock.location', string='Location', copy=True, store=True)

    def add_generalization(self):
        pass
