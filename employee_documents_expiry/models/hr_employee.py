from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    document_counter = fields.Integer(string='# Documents', readonly=True)

    def document_view(self):
        pass