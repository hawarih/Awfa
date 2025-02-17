from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    check_list_enable = fields.Boolean(string='Check List Enable', store=True)
    entry_checklist_ids = fields.Many2many(comodel_name='employee.checklist', string='Entry Process', copy=True, relation='entry_obj_ids', column1='check_hr_rel', column2='hr_check_rel', store=True)
    entry_progress = fields.Float(string='Entry Progress', readonly=True, store=True)
    exit_checklist_ids = fields.Many2many(comodel_name='employee.checklist', string='Exit Process', copy=True, relation='exit_obj_ids', column1='exit_hr_rel', column2='hr_exit_rel', store=True)
    exit_progress = fields.Float(string='Exit Progress', readonly=True, store=True)
    maximum_rate = fields.Integer(string='Maximum Rate', copy=True, store=True)
