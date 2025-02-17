from odoo import api, fields, models


class HrDepartment(models.Model):
    _inherit = 'hr.department'

    def get_related_employees(self):
        pass