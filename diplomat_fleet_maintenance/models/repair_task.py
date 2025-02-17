from odoo import api, fields, models


class RepairTask(models.Model):
    _name = 'repair.task'
    _description = 'Repair Task'

    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', readonly=True,  store=True)
    expected_cost_by_hour = fields.Float(string='Expected Cost By Hour', copy=True, store=True)
    expected_no_of_workers = fields.Integer(string='Expected No Of Workers', copy=True, store=True)
    expected_total_cost = fields.Monetary(string='Expected Total Cost', readonly=True)
    expected_work_hours = fields.Float(string='Expected Work Hours', copy=True, store=True)
    maintenance_workshop_ids = fields.Many2many(comodel_name='maintenance.workshop', string='Maintenance Workshop', copy=True, relation='maintenance_workshop_repair_task_rel', column1='repair_task_id', column2='maintenance_workshop_id', store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    spare_part_ids = fields.Many2many(comodel_name='product.template', string='Spare Part', copy=True, relation='product_template_repair_task_rel', column1='repair_task_id', column2='product_template_id', store=True)
