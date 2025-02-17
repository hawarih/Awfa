from odoo import api, fields, models


class HrJob(models.Model):
    _inherit = 'hr.job'

    code = fields.Char(string='Code', copy=True, store=True)


    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Code must be unique')
    ]