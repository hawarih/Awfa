from odoo import api, fields, models


class AuthorizationCountry(models.Model):
    _name = 'authorization.country'
    _description = 'Authorization Country'

    ar_name = fields.Char(string='Arabic Name', copy=True, required=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    naql_code = fields.Char(string='Naql Code', copy=True, required=True, store=True)
    naql_id = fields.Char(string='Naql', copy=True, required=True, store=True)
