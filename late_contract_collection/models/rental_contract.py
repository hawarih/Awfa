from odoo import api, fields, models


class RentalContract(models.Model):
    _inherit = 'rental.contract'

    arrest_warrant_canceled = fields.Boolean(string='Arrest Warrant Canceled', copy=True, store=True)
    cancel_arrest_warrant_ids = fields.One2many(comodel_name='cancel.arrest.warrant', inverse_name='rental_contract_id', string='Cancel Arrest Warrant', store=True)
    duration_late_contract = fields.Integer(string='Duration Late Contract', readonly=True)
    generalization_ids = fields.One2many(comodel_name='generalization', inverse_name='rental_contract_id', string='Generalization', store=True)
    is_generalized = fields.Boolean(string='Is Generalized', copy=True, store=True)
    is_waiting_generalization = fields.Boolean(string='Is Waiting Generalization', copy=True, store=True)
    last_statement = fields.Text(string='Last Statement', copy=True, store=True)
    last_statement_date = fields.Datetime(string='Last Statement Date', copy=True, store=True)
    late_entry_time = fields.Date(string='Late Entry Time', readonly=True)
    statement_ids = fields.One2many(comodel_name='statement', inverse_name='rental_contract_id', string='Statement', store=True)
