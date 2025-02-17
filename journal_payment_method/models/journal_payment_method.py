from odoo import api, fields, models


class JournalPaymentMethod(models.Model):
    _name = 'journal.payment.method'
    _description = 'Journal Payment Method'

    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, store=True)
