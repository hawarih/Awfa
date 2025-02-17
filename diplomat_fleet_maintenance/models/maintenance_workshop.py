from odoo import api, fields, models


class MaintenanceWorkshop(models.Model):
    _name = 'maintenance.workshop'
    _description = 'Maintenance Workshop'

    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
