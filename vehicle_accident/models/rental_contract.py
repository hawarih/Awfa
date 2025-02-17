from odoo import api, fields, models


class RentalContract(models.Model):
    _inherit = 'rental.contract'

    accident_vehicle_ids = fields.Many2one(comodel_name='vehicle.accident', string='Accident Vehicle', copy=True, store=True)
    is_accident = fields.Boolean(string='Is Accident', copy=True, store=True)
