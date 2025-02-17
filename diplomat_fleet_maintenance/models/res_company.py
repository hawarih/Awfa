from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    accident_manager = fields.Many2many(comodel_name='res.users', string='Accident Manager', copy=True, relation='res_company_res_users_rel', column1='res_company_id', column2='res_users_id', store=True)
