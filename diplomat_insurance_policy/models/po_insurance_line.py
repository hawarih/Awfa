from odoo import api, fields, models


class PoInsuranceLine(models.TransientModel):
    _name = 'po.insurance.line'
    _description = 'Po Insurance Line'

    current_date = fields.Date(string='Current Date', copy=True, store=True)
    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', copy=True, required=True, ondelete='cascade', store=True)
    insurance_line_ids = fields.Many2many(comodel_name='purchase.order.line', string='Insurance Line', copy=True, relation='po_insurance_line_purchase_order_line_rel', column1='po_insurance_line_id', column2='purchase_order_line_id', store=True)
    insurance_value = fields.Float(string='Insurance Value', copy=True, store=True)
    purchase_id = fields.Many2one(comodel_name='purchase.order', string='PO', copy=True, store=True)

    def add_insurance(self):
        pass