from odoo import api, fields, models


class BranchBranch(models.Model):
    _inherit = 'branch.branch'

    work_location_id = fields.Many2one(comodel_name='hr.work.location', string='Work Location', copy=True,  store=True)
