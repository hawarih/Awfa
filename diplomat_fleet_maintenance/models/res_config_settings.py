from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    accident_manager_notification = fields.Many2many(comodel_name='res.users', string='Accident Manager', related='company_id.accident_manager')
    external_maintenance_product_id = fields.Many2one(comodel_name='product.product', string='External Maintenance Product', copy=True,  store=True)
    insurance_maintenance_product_id = fields.Many2one(comodel_name='product.product', string='Insurance Maintenance Product', copy=True,  store=True)
    maintenance_journal_id = fields.Many2one(comodel_name='account.journal', string='Maintenance Journal', copy=True,  store=True)
