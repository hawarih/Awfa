from odoo import api, fields, models


class PreventiveMaintenancePlan(models.Model):
    _name = 'preventive.maintenance.plan'
    _description = 'Preventive Maintenance Plan'

    kilometer = fields.Integer(string='Kilometer', copy=True, store=True)
    model_ids = fields.Many2many(comodel_name='fleet.vehicle.model', string='Model', copy=True, relation='fleet_vehicle_model_preventive_maintenance_plan_rel', column1='preventive_maintenance_plan_id', column2='fleet_vehicle_model_id', store=True)
    months = fields.Integer(string='Months', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    notification_user_ids = fields.Many2many(comodel_name='res.users', string='Notification User', copy=True, relation='preventive_maintenance_plan_res_users_rel', column1='preventive_maintenance_plan_id', column2='res_users_id', store=True)
    repair_task_ids = fields.Many2many(comodel_name='repair.task', string='Repair Task', copy=True, relation='preventive_maintenance_plan_repair_task_rel', column1='preventive_maintenance_plan_id', column2='repair_task_id', store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('confirm', 'In Progress'), ('cancel', 'Cancelled')], store=True, default='draft')

    def confirm(self):
        pass

    def cancel(self):
        pass
