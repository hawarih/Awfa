from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    customer = fields.Boolean(string='Is Customer', copy=True, related="partner_id.customer")
    driver = fields.Boolean(string='Driver / shipping co', copy=True, related="partner_id.driver")
    supplier = fields.Boolean(string='Is Supplier', copy=True, related="partner_id.supplier")
