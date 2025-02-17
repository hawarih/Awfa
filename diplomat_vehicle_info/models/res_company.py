from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    id_no = fields.Char(string='ID No.', copy=True, store=True)
