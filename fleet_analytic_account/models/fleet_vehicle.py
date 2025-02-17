from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    analytic_account_id = fields.Many2one(comodel_name='account.analytic.account', string='Analytic Account', copy=True, store=True)
    create_analytic = fields.Boolean(string='Create Analytic', copy=True, store=True)
