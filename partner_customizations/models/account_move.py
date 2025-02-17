from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    partner_id_rel = fields.Many2one(comodel_name='res.partner', string='Partner', readonly=True)