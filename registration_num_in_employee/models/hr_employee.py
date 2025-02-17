from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    address_id = fields.Many2one(comodel_name='res.partner', string='Work Address', copy=True, ondelete='set null', store=True)
    identification_number = fields.Char(string='Identification Number', related='registration_number_id.identification_number', readonly=True)
    insurance = fields.Text(string='Insurance subscription number for employee', copy=True, store=True)
    insurance_subscription_number = fields.Char(string='Insurance Subscription Number', related='registration_number_id.insurance_subscription_number', readonly=True)
    labour_office_number = fields.Char(string='Labour Office Number', related='registration_number_id.labour_office_number', readonly=True)
    location = fields.Text(string='Location', related='registration_number_id.location', readonly=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', readonly=True, ondelete='set null')
    registration_number_id = fields.Many2one(comodel_name='register.number', string='Registration Number', copy=True, ondelete='set null', store=True)
