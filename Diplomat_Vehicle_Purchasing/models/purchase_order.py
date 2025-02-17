from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active_not_paid = fields.Boolean(string='Active Not Paid', readonly=True)
    active_paid = fields.Boolean(string='Active Paid', readonly=True)
    active_partial = fields.Boolean(string='Active Partial', readonly=True)
    add_insurance = fields.Boolean(string='Add Insurance', related='purchase_type_id.add_insurance', readonly=True)
    all_types = fields.Boolean(string='All Types', readonly=True)
    allow_create_vehicle = fields.Boolean(string='Allow Create Vehicle from PO', related='purchase_type_id.allow_create_vehicle', readonly=True)
    allowed_down_payment = fields.Float(string='Allowed Down Payments', readonly=True)
    cash_purchasing = fields.Boolean(string='Cash Purchasing', related='purchase_type_id.cash_purchasing', readonly=True)
    check_install = fields.Boolean(string='Check Install', copy=True, store=True)
    check_invoice = fields.Boolean(string='Check Invoice', readonly=True)
    check_line_state = fields.Boolean(string='Check Line State', readonly=True)
    create_vehicle_po = fields.Boolean(string='Allow Create Vehicle From PO', related='purchase_type_id.allow_create_vehicle', readonly=True)
    down_payment = fields.Float(string='Down Payments', copy=True, store=True)
    final_total = fields.Float(string='Total', readonly=True)
    installment_date = fields.Date(string='First Installment Date', readonly=True)
    installment_ids = fields.One2many(comodel_name='installment.line', inverse_name='purchase_id', string='Installment Lines', store=True)
    interest_amount = fields.Float(string='Interest Amount', copy=True, store=True)
    is_leasing = fields.Boolean(string='Is Leasing', related='purchase_type_id.is_leasing', readonly=True)
    no_months = fields.Integer(string='No of Months Without Interest', copy=True, store=True)
    number_installment = fields.Integer(string='Number of Installment', copy=True, store=True)
    owner_ship_amount = fields.Float(string='Ownership Amount', readonly=True)
    owner_ship_check = fields.Boolean(string='Owner Ship Check', readonly=True)
    payment_count = fields.Integer(string='payments', readonly=True)
    payment_ids = fields.One2many(comodel_name='account.payment', inverse_name='purchase_order_id', string='Payment', readonly=True)
    payment_instalment = fields.Boolean(string='Payment Instalment', related='purchase_type_id.payment_instalment', readonly=True)
    price_sum = fields.Float(string='price_sum', readonly=True)
    purchase_type_id = fields.Many2one(comodel_name='purchase.type', string='Purchase Order Type', copy=True, required=True, ondelete='restrict', store=True)
    remaining = fields.Float(string='Remaining', readonly=True)
    show_add_insurance = fields.Boolean(string='Show Add Insurance', readonly=True)
    show_create_down_payment = fields.Boolean(string='Show Create Down Payment', readonly=True)
    start_date = fields.Date(string='Contract Start Date', copy=True, store=True)
    tax_admin_fee = fields.Many2one(comodel_name='account.tax', string='Taxes %', copy=True, readonly=True, ondelete='set null', store=True)
    tax_insurance = fields.Many2one(comodel_name='account.tax', string='Taxes %', copy=True, readonly=True, ondelete='set null', store=True)
    tax_interest = fields.Many2one(comodel_name='account.tax', string='Taxes %', copy=True, ondelete='set null', store=True)
    tax_plates_fee = fields.Many2one(comodel_name='account.tax', string='Taxes %', copy=True, ondelete='set null', store=True)
    total_admin_after_taxes = fields.Float(string='Total', readonly=True)
    total_insurance_after_taxes = fields.Float(string='Total', readonly=True)
    total_interest_after_taxes = fields.Float(string='Total', readonly=True)
    total_payment = fields.Float(string='Total Payment', readonly=True)
    total_plates_after_taxes = fields.Float(string='Total', readonly=True)
    type = fields.Selection(string='Type', selection=[], related='purchase_type_id.type', readonly=True)
    untaxed_total_admin_fee = fields.Float(string='Untaxed Amount', readonly=True)
    untaxed_total_insurance = fields.Float(string='Untaxed Amount', readonly=True)
    untaxed_total_interest = fields.Float(string='Untaxed Amount', readonly=True)
    untaxed_total_plates_fee = fields.Float(string='Untaxed Amount', readonly=True)
    vehicle_count = fields.Integer(string='Vehicles', readonly=True)

    def create_vehicle(self):
        pass

    def create_bill_info(self):
        pass

    def delete_vehicle(self):
        pass

    def create_down_payment(self):
        pass

    def create_install(self):
        pass

    def print_vehicle_excel(self):
        pass

    def delete_vehicle(self):
        pass

    def get_vehicles(self):
        pass

    def get_payment(self):
        pass
