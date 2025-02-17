from odoo import api, fields, models


class VehicleDamageLines(models.Model):
    _name = 'vehicle.damage.lines'
    _description = 'Vehicle Damage Lines'

    amount = fields.Float(string='Amount', copy=True, store=True)
    repair_task = fields.Text(string='Repair Task', copy=True, store=True)
    vehicle_damage_id = fields.Many2one(comodel_name='vehicle.damage', string='Vehicle Damage', copy=True, store=True)
