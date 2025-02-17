from odoo import api, fields, models


class MobileTermsPolicy(models.Model):
    _name = 'mobile.terms.policy'
    _description = 'Mobile Terms Policy'

    name = fields.Char(string='Name', copy=True, required=True, store=True)
    privacy_policy = fields.Html(string='Privacy Policy', copy=True, required=True, translate=True, store=True)
    terms_conditions = fields.Html(string='Terms And Conditions', copy=True, required=True, translate=True, store=True)
