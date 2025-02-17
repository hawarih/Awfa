from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    maintenance_team_ids = fields.Many2many(comodel_name='maintenance.team', string='Maintenance Team', copy=True, relation='maintenance_team_users_rel', column1='res_users_id', column2='maintenance_team_id', store=True)
