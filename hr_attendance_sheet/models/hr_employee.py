from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    code = fields.Char(string='Code', copy=True, store=True)

    
    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Code must be unique')
    ]