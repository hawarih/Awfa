from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', copy=True, store=True)
