from odoo import api, fields, models


class InstallmentLine(models.Model):
    _name = 'installment.line'
    _description = 'Installment Line'

    amount = fields.Float(string='Monthly Amount', copy=True, store=True)
    due_date = fields.Date(string='date', copy=True, store=True)
    no_installment = fields.Integer(string='No', copy=True, store=True)
    owner_check = fields.Boolean(string='owner check', copy=True, store=True)
    owner_ship_check = fields.Boolean(string='Owner Ship Check', readonly=True)
    paid = fields.Float(string='Paid', copy=True, store=True)
    paid_amount = fields.Float(string='Amount', copy=True, store=True)
    po_name = fields.Char(string='PO Number', related='purchase_id.name', readonly=True)
    purchase_id = fields.Many2one(comodel_name='purchase.order', string='Purchase', copy=True, ondelete='set null', store=True)
    remaining = fields.Float(string='Remaining', readonly=True)
    state = fields.Selection(string='Status', selection=[('not_paid', 'Not Paid'), ('partial', 'Partial'), ('paid', 'Paid')], readonly=True)

    def create_payment(self):
        pass
