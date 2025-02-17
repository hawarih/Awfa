from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    date_end_hijri = fields.Char(string='Contract End Date Hijri', readonly=True)
    date_start_hijri = fields.Char(string='Start Hijri Date', readonly=True)
    department_id = fields.Many2one(comodel_name='hr.department', string='Department', related='employee_id.department_id', readonly=True, store=True)
    end_date = fields.Date(string='End Date', copy=True, store=True)
    end_date_hijri = fields.Char(string='End Hijri Date', readonly=True)
    structure_type_id = fields.Many2one(comodel_name='hr.payroll.structure.type', string='Salary Structure Type', related='struct_id.type_id', readonly=True)

    def notification_end_date(self):
        pass
