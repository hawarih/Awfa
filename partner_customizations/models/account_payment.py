from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountPayments(models.Model):
    _inherit = 'account.payment'

    available_partner_ids = fields.Many2many(comodel_name='res.partner', string="Available Partner", readonly=True)
    partner_id = fields.Many2one(string='Customer/Vendor', comodel_name='res.partner', store=True, copy=True, ondelete='restrict')
    partner_id_rel = fields.Many2one(comodel_name='res.partner', string='Partner', readonly=True, related='move_id.partner_id_rel')
