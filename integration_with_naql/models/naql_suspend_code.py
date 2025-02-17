from odoo import api, fields, models


class NaqlSuspendCode(models.Model):
    _name = 'naql.suspend.code'
    _description = 'Naql Suspend Code'

    arabic_name = fields.Char(string='Arabic Name', copy=True, required=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    naql_code = fields.Char(string='Naql Code', copy=True, required=True, store=True)
    naql_id = fields.Char(string='Naql Id', copy=True, required=True, store=True)
