from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    resource_calendar_id = fields.Many2one(comodel_name='resource.calendar', string='Working Schedule', help="""Employee's working schedule.""", related='employee_id.resource_calendar_id', required=True, readonly=True, index=True, store=True)
