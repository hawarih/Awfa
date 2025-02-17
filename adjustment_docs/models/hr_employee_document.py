from odoo import api, fields, models


class HrEmployeeDocument(models.Model):
    _inherit = 'hr.employee.document'

    before_days = fields.Integer(string='Days Before', copy=True, store=True)
    doc_type = fields.Selection(string='Checklist Type', selection=[], related='document_name.document_type', readonly=True)
    users_ids = fields.Many2many(comodel_name='res.users', string='Users', copy=True, relation='hr_employee_document_res_users_rel', column1='hr_employee_document_id', column2='res_users_id', store=True)
