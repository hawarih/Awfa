from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    insurance_count = fields.Integer(string='Insurance Count', readonly=True)
    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, store=True)

    def action_add_insurance(self):
        pass
    
    def action_open_insurance(self):
        pass