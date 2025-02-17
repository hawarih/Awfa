from odoo import api, fields, models


class MaintenanceStage(models.Model):
    _inherit = 'maintenance.stage'

    cancel = fields.Boolean(string='Cancel', copy=True, store=True)
    close = fields.Boolean(string='Close', copy=True, store=True)
    confirm = fields.Boolean(string='Confirm', copy=True, store=True)
    reset_to_draft = fields.Boolean(string='Reset To Draft', copy=True, store=True)
