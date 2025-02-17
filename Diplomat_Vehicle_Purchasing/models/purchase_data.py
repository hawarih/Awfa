from odoo import api, fields, models


class PurchaseData(models.TransientModel):
    _name = 'purchase.data'
    _description = 'Purchase Data'

    admin_fee = fields.Float(string='Adminstrative Fee', copy=True, store=True)
    insurance = fields.Float(string='Insurance Value', copy=True, store=True)
    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, ondelete='set null', store=True)
    model_id = fields.Many2one(comodel_name='fleet.vehicle.model', string='Model', copy=True, ondelete='set null', store=True)
    owner_ship = fields.Float(string='Ownership Value', copy=True, store=True)
    plates_fee = fields.Float(string='Plates Fees', copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', copy=True, ondelete='set null', store=True)
    purchase_id = fields.Many2one(comodel_name='bill.information.wizard', string='Purchase', copy=True, ondelete='set null', store=True)
