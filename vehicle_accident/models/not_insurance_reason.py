from odoo import api, fields, models


class NotInsuranceReason(models.Model):
    _name = 'not.insurance.reason'
    _description = 'Not Insurance Reason'

    name = fields.Char(string='Name', copy=True, store=True)
