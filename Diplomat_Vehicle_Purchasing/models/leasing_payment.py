from odoo import api, fields, models


class LeasingPayment(models.TransientModel):
    _name = 'leasing.payment'
    _description = 'Leasing Payment'

    administrative_fee = fields.Boolean(string='Administrative Fee', copy=True, store=True)
    amount = fields.Float(string='Amount', copy=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    down_payment = fields.Boolean(string='Down Payment', copy=True, store=True)
    final_amount = fields.Float(string='Final Amount', copy=True, store=True)
    install_id = fields.Many2one(comodel_name='installment.line', string='Install Line', copy=True, ondelete='set null', store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, ondelete='set null', store=True)
    memo = fields.Char(string='Memo', copy=True, store=True)
    payment_method_line_id = fields.Many2one(comodel_name='account.payment.method.line', string='Payment Method Line', readonly=True, ondelete='set null')
    plate_fees = fields.Boolean(string='Plate Fees', copy=True, store=True)
    purchase_id = fields.Many2one(comodel_name='purchase.order', string='Purchase Order', copy=True, ondelete='set null', store=True)
    readonly_amount = fields.Boolean(string='Readonly Amount', copy=True, store=True)
    type = fields.Selection(string='Type', selection=[('entry', 'Entry'), ('payment', 'Payment'), ('contract_payment', 'Contract Payment')], copy=True, store=True)
    vehicle_contract_line_id = fields.Many2one(comodel_name='_unknown', string='Vehicle Contract Line', copy=True, ondelete='set null', store=True)
    vendor_id = fields.Many2one(comodel_name='res.partner', string='Vendor', copy=True, ondelete='set null', store=True)

    def create_payment(self):
        pass
