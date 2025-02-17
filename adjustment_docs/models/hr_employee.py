from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    active = fields.Boolean(string='Active', help="""If the active field is set to False, it will allow you to hide the resource record without removing it.""", related='resource_id.active', store=True)
    document_count_new = fields.Integer(string='Document Count New', readonly=True)
    entry_checklist = fields.Many2many(comodel_name='employee.checklist', relation="entry_checklist_rel", column1='employee_id', column2='checklist_id', string='Entry Process')
    exit_checklist = fields.Many2many(comodel_name='employee.checklist', relation="exit_checklist_rel", column1='employee_id', column2='checklist_id', string='Exit Process')
    hr_employee_document_ids = fields.One2many(comodel_name='hr.employee.document', inverse_name='employee_ref', string='Hr Employee Document', store=True)


    def document_view(self):
        pass
    
    
class EmployeeChecklist(models.Model):
    _inherit = 'employee.checklist'

    entry_checklist_rel = fields.Many2many(comodel_name='hr.employee', relation="entry_checklist", column1='checklist_id', column2='employee_id', string='Entry Process')
    exit_checklist_rel = fields.Many2many(comodel_name='hr.employee', relation="exit_checklist", column1='checklist_id', column2='employee_id', string='Exit Process')
