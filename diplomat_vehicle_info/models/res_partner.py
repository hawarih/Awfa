from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    id_no = fields.Char(string='ID No.', copy=True, store=True)
