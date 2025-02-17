from odoo import api, fields, models


class InstallmentBatchPayment(models.Model):
    _name = 'installment.batch.payment'
    _description = 'Installment Batch Payment'

    amount = fields.Float(string='Amount', copy=True, store=True)
    date_from = fields.Date(string='Date From', copy=True, store=True)
    date_to = fields.Date(string='Date To', copy=True, store=True)
    installment_ids = fields.Many2many(comodel_name='installment.line', string='Installment', copy=True, relation='installment_batch_payment_installment_line_rel', column1='installment_batch_payment_id', column2='installment_line_id', store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, store=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Vendor', copy=True, store=True)
    payment_count = fields.Integer(string='Payment Count', readonly=True)
    purchase_order_ids = fields.Many2many(comodel_name='purchase.order', string='Purchase Order', copy=True, relation='installment_batch_payment_purchase_order_rel', column1='installment_batch_payment_id', column2='purchase_order_id', store=True)
    remaining_amount = fields.Float(string='Remaining Amount', copy=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirmed'), ('close', 'Paid'), ('cancel', 'Cancelled')],
                                                    default='draft', store=True)
    total_remaining = fields.Float(string='Total', readonly=True)

    def action_generate(self):
        pass
    
    def action_confirm(self):
        pass
    
    def action_close(self):
        pass
    
    def action_cancel(self):
        pass
    
    def action_draft(self):
        pass
    
    def action_view_payment(self):
        pass
