from odoo import api, fields, models


class HrWorkLocation(models.Model):
    _inherit = 'hr.work.location'

    allowed_distance = fields.Float(string='Allowed Distance', copy=True, required=True, store=True)
    latitude = fields.Float(string='Latitude', copy=True, required=True, store=True)
    longitude = fields.Float(string='Longitude', copy=True, required=True, store=True)
