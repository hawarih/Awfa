from odoo import api, fields, models


class AllowedAttendanceLocation(models.Model):
    _name = 'allowed.attendance.location'
    _description = 'Allowed Attendance Location'

    allowed_distance = fields.Float(string='Allowed Distance', copy=True, required=True, store=True)
    latitude = fields.Float(string='Latitude', copy=True, required=True, store=True)
    longitude = fields.Float(string='Longitude', copy=True, required=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, store=True)
