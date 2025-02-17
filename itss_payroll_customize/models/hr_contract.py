from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    assigned = fields.Float(string='Assigned', copy=True, store=True)
    assigned_from = fields.Date(string='Assigned From', copy=True, store=True)
    assigned_readonly = fields.Boolean(string='Assigned Readonly', copy=True, store=True)
    assigned_to = fields.Date(string='Assigned To', copy=True, store=True)
    bonus = fields.Float(string='Bonus', copy=True, store=True)
    call = fields.Float(string='Call', copy=True, store=True)
    education = fields.Float(string='Education', copy=True, store=True)
    food = fields.Float(string='Food', copy=True, store=True)
    gosi = fields.Float(string='GOSI', copy=True, store=True)
    housing = fields.Float(string='Housing', copy=True, store=True)
    is_assigned = fields.Boolean(string='Is Assigned', copy=True, store=True)
    job_nature = fields.Float(string='Job Nature', copy=True, store=True)
    other = fields.Float(string='Other', copy=True, store=True)
    other_allowance_line_ids = fields.One2many(comodel_name='hr.other.allowance.line', inverse_name='contract_id', string='Other Allowance Line', store=True)
    personal_car_usage = fields.Float(string='Personal Car Usage', copy=True, store=True)
    transportation = fields.Float(string='Transportation', copy=True, store=True)

    def action_confirm_assigned_dates(self):
        pass

    def action_confirm_assigned_dates(self):
        pass
