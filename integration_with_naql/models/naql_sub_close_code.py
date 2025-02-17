from odoo import api, fields, models


class NaqlSubCloseCode(models.Model):
    _name = 'naql.sub.close.code'
    _description = 'Naql Sub Close Code'

    arabic_name = fields.Char(string='Arabic Name', copy=True, required=True, store=True)
    main_close_reason_id = fields.Many2one(comodel_name='naql.main.close.code', string='Main Reason', copy=True, required=True, ondelete='restrict', store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    naql_code = fields.Char(string='Naql Code', copy=True, required=True, store=True)
    naql_id = fields.Char(string='Naql Id', copy=True, required=True, store=True)
