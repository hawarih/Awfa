from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    user_ids = fields.Many2many(comodel_name='res.users', string='Accepted Users', copy=True, relation='res_company_users_rel', column1='cid', column2='user_id', store=True)
