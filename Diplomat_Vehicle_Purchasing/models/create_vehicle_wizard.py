from odoo import api, fields, models


class CreateVehicleWizard(models.TransientModel):
    _name = 'create.vehicle.wizard'
    _description = 'Create Vehicle Wizard'

    vehicle_ids = fields.One2many(comodel_name='vehicle.data', inverse_name='vehicle_id', string='Vehicle Information', store=True)

    def create_vehicles(self):
        pass