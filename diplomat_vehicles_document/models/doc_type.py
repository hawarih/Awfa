from odoo import api, fields, models


class DocType(models.Model):
    _name = 'doc.type'
    _description = 'Doc Type'

    is_licence = fields.Boolean(string='Is Licence', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, store=True)
