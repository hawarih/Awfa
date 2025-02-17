from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    purchase_requisition_ids = fields.Many2many(comodel_name='material.purchase.requisition', string='Material Purchase Requisition', copy=True, relation='material_purchase_requisition_rel', column1='res_users_id', column2='material_purchase_requisition_id', store=True)
