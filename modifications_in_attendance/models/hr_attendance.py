from odoo import api, fields, models


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    branch_id = fields.Many2one(comodel_name='branch.branch', string='Branch', related='employee_id.branch_id', readonly=True, store=True)
    department_id = fields.Many2one(comodel_name='hr.department', string='Department', related='employee_id.department_id', readonly=True, store=True)
    job_id = fields.Many2one(comodel_name='hr.job', string='Job Position', related='employee_id.job_id', readonly=True, store=True)
