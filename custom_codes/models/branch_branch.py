from odoo import api, fields, models


class BranchBranch(models.Model):
    _name = 'branch.branch'
    _description = 'Branch Branch'

    code = fields.Char(string='Code', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    
    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Code must be unique'),
    ]
