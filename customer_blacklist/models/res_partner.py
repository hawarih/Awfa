from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    blacklist_by = fields.Many2one(comodel_name='res.users', string='Blacklist By', copy=True, store=True)
    blacklist_type = fields.Selection(string='Blacklist Type', selection=[('no_message', 'No Message'), ('warning', 'Warning'), ('blocking_message', 'Blocking Message')], 
                                      default='no_message', copy=True, required=True, store=True)
    date = fields.Date(string='Date', copy=True, readonly=True, index=True, store=True)
    is_blacklist = fields.Boolean(string='Blacklist', readonly=True, )
    is_warning = fields.Boolean(string='Warning', readonly=True, )
    message = fields.Text(string='Message', copy=True, store=True)
    warning_by = fields.Many2one(comodel_name='res.users', string='Warning By', copy=True, store=True)
