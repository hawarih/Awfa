from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    blacklist_by = fields.Many2one(comodel_name='res.users', string='Blacklist By', copy=True, related='partner_id.blacklist_by')
    blacklist_type = fields.Selection(string='Blacklist Type', selection=[], copy=True, related='partner_id.blacklist_type', required=True)
    date = fields.Date(string='Date', copy=True, related='partner_id.date', readonly=True)
    is_blacklist = fields.Boolean(string='Blacklist', related='partner_id.is_blacklist', readonly=True)
    is_warning = fields.Boolean(string='Warning', related='partner_id.is_warning', readonly=True)
    message = fields.Text(string='Message', copy=True, related='partner_id.message')
    warning_by = fields.Many2one(comodel_name='res.users', string='Warning By', copy=True, related='partner_id.warning_by')
