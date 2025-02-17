from odoo import api, fields, models


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    check_in_latitude = fields.Float(string='Check In Latitude', copy=True, store=True)
    check_in_longitude = fields.Float(string='Check In Longitude', copy=True, store=True)
    check_in_state = fields.Selection(string='Check In State', selection=[('normal', 'Normal'), ('late', 'Late'), ('week_end', 'Week End'), ('holiday', 'Public Holiday')], 
                                        default='normal',readonly=True)
    check_out_latitude = fields.Float(string='Check Out Latitude', copy=True, store=True)
    check_out_longitude = fields.Float(string='Check Out Longitude', copy=True, store=True)
    check_out_state = fields.Selection(string='Check Out State', selection=[('normal', 'Normal'), ('diff', 'Difference'), ('week_end', 'Week End'), ('holiday', 'Public Holiday'), ('over_time', 'Over Time')], 
                                        default='normal',readonly=True)
