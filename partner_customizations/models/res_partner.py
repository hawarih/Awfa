from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    customer = fields.Boolean(string='Is Customer', store=True, copy=True, default=True)
    driver = fields.Boolean(string='Driver / shipping co', store=True, copy=True)
    supplier = fields.Boolean(string='Is Supplier', store=True, copy=True)
