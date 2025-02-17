from odoo import api, fields, models


class PurchaseType(models.Model):
    _name = 'purchase.type'
    _description = 'Purchase Type'

    add_insurance = fields.Boolean(string='Add Insurance', copy=True, store=True)
    allow_create_vehicle = fields.Boolean(string='Allow Create Vehicle from PO', copy=True, store=True)
    borrowed = fields.Boolean(string='Borrowed', copy=True, store=True)
    cash_purchasing = fields.Boolean(string='Cash Purchasing', copy=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, ondelete='set null', store=True)
    insurance_product = fields.Many2one(comodel_name='product.template', string='Insurance Product', copy=True, ondelete='set null', store=True)
    interest_product = fields.Many2one(comodel_name='product.template', string='Interest Product', copy=True, ondelete='set null', store=True)
    is_leasing = fields.Boolean(string='Is Leasing', copy=True, store=True)
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal', copy=True, ondelete='set null', store=True)
    name = fields.Char(string='Name', copy=True, store=True)
    payment_instalment = fields.Boolean(string='Payment Instalment', copy=True, store=True)
    plates_fee_id = fields.Many2one(comodel_name='product.template', string='Plates Fee Product', copy=True, ondelete='set null', store=True)
    type = fields.Selection(string='Type', selection=[('vehicle', '  Vehicle'), ('spar', 'Spare Parts')], copy=True, store=True)
