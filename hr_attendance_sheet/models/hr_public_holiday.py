from odoo import api, fields, models


class HrPublicHoliday(models.Model):
    _name = 'hr.public.holiday'
    _description = 'Hr Public Holiday'

    date_from = fields.Date(string='From', copy=True, store=True)
    date_to = fields.Date(string='To', copy=True, store=True)
    name = fields.Char(string='Reason', copy=True, store=True)
    note = fields.Text(string='Notes', copy=True, store=True)
    state = fields.Selection(string='Status', selection=[('active', 'Active'), ('inactive', 'Not Active')], 
                             default='inactive', required=True, index=True, store=True)
