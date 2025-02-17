from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    id_no = fields.Char(string='ID No.', copy=True, related='partner_id.id_no')
