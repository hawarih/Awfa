from odoo import api, fields, models


class MaintenanceRepairTaskLine(models.Model):
    _name = 'maintenance.repair.task.line'
    _description = 'Maintenance Repair Task Line'

    done = fields.Boolean(string='Done', copy=True, store=True)
    maintenance_id = fields.Many2one(comodel_name='maintenance.request', string='Maintenance', copy=True,  store=True)
    repair_task_id = fields.Many2one(comodel_name='repair.task', string='Repair Task', copy=True,  store=True)
    spare_part_ids = fields.Many2many(comodel_name='product.template', string='Spare Part', related='repair_task_id.spare_part_ids', readonly=True)
    workers_ids = fields.Many2many(comodel_name='hr.employee', string='Workers', copy=True, relation='hr_employee_maintenance_repair_task_line_rel', column1='maintenance_repair_task_line_id', column2='hr_employee_id', store=True)

    def check_task(self):
        pass

    def check_task(self):
        pass
