from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    fam_ids = fields.One2many(comodel_name='hr.employee.family', inverse_name='employee_id', string='Family', help="""Family Information""", store=True)
    id_attachment_id = fields.Many2many(comodel_name='ir.attachment', string='Attachment', help="""You can attach the copy of your Id""", copy=True, relation='id_attachment_rel', column1='id_ref', column2='attach_ref', store=True)
    id_expiry_date = fields.Date(string='Expiry Date', help="""Expiry date of Identification ID""", copy=True, store=True)
    joining_date = fields.Date(string='Joining Date', help="""Employee joining date computed from the contract start date""", readonly=True, store=True)
    passport_attachment_id = fields.Many2many(comodel_name='ir.attachment', string='Attachment', help="""You can attach the copy of Passport""", copy=True, relation='passport_attachment_rel', column1='passport_ref', column2='attach_ref1', store=True)
    passport_expiry_date = fields.Date(string='Expiry Date', help="""Expiry date of Passport ID""", copy=True, store=True)
    personal_mobile = fields.Char(string='Mobile', help="""Personal mobile number of the employee""", related='address_home_id.mobile', readonly=True, store=True, )
