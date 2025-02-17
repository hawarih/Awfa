from odoo import api, fields, models


class HrWorkLocation(models.Model):
    _inherit = 'hr.work.location'

    address_id = fields.Many2one(comodel_name='res.partner', string='Work Address', copy=True, required=True, ondelete='restrict', store=True)
