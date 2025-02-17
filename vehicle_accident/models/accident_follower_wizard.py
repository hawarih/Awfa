from odoo import api, fields, models


class AccidentFollowerWizard(models.TransientModel):
    _name = 'accident.follower.wizard'
    _description = 'Accident Follower Wizard'

    follower_id = fields.Many2one(comodel_name='hr.employee', string='Follower', copy=True, store=True)
    vehicle_accident_id = fields.Many2one(comodel_name='vehicle.accident', string='Vehicle Accident', copy=True, store=True)

    def action_confirm(self):
        pass
