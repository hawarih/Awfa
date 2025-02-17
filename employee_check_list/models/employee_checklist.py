from odoo import api, fields, models


class EmployeeChecklist(models.Model):
    _inherit = 'employee.checklist'

    entry_obj_ids = fields.Many2many(comodel_name='hr.employee', string='Entry Obj', copy=True, relation='entry_checklist_ids', column1='hr_check_rel', column2='check_hr_rel', store=True)
    exit_obj_ids = fields.Many2many(comodel_name='hr.employee', string='Exit Obj', copy=True, relation='exit_checklist_ids', column1='hr_exit_rel', column2='exit_hr_rel', store=True)
