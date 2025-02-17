from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    code = fields.Char(string='Code', copy=True, store=True)


    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Code must be unique')
    ]
