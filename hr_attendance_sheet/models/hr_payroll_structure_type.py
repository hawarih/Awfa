from odoo import api, fields, models


class HrPayrollStructureType(models.Model):
    _inherit = 'hr.payroll.structure.type'

    default_work_entry_type_id = fields.Many2one(comodel_name='hr.work.entry.type', string='Default Work Entry Type', help="""Work entry type for regular attendances.""", copy=True, store=True)
