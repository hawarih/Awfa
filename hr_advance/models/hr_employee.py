from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    address_home_id = fields.Many2one(comodel_name='res.partner', string='Private Address', help="""Enter here the private address of the employee, not the one linked to your company.""", copy=True, store=True)
    advance_amount = fields.Float(string='Advance Amount', copy=True, readonly=True, store=True)
