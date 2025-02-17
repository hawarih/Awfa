from odoo import api, fields, models


class UsageType(models.Model):
    _name = 'usage.type'
    _description = 'Usage Type'

    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    tajeer_id = fields.Char(string='Tajeer', copy=True, store=True)


    _sql_constraints = [
        ('tajeer_id_uniq', 'unique(tajeer_id)', 'Tajeer ID must be unique'),
        ('name_uniq', 'unique(name)', 'Name must be unique'),
    ]