from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    dest_location_id = fields.Many2one(comodel_name='stock.location', string='Destination Location', copy=True, store=True)
