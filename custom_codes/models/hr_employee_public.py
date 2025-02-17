from odoo import api, fields, models


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    branch_code = fields.Char(string='Branch Code', related='branch_id.code', readonly=True)
    branch_id = fields.Many2one(comodel_name='branch.branch', string='Branch', copy=True, store=True)
    children = fields.Integer(string='Number of Family', copy=True, store=True)
    code = fields.Char(string='Code', copy=True, store=True)
    company_code = fields.Char(string='Company Code', related='company_id.code', readonly=True)
    department_code = fields.Char(string='Department Code', related='department_id.code', readonly=True)
    employee_group_id = fields.Many2one(comodel_name='employee.group', string='Employee Group', copy=True, store=True)
    employee_subgroup_id = fields.Many2one(comodel_name='employee.subgroup', string='Employee Subgroup', copy=True, store=True)
    employee_type = fields.Selection(string='Employee Type', help="""The employee type. Although the primary purpose may seem to categorize employees, this field has also an impact in the Contract History. Only Employee type is supposed to be under contract and will have a Contract History.""", selection=[('employee', 'Employee'), ('al_raya_employee', 'Al Raya Employee'), ('student', 'Student'), ('raya_al_ajelah', 'Raya Al Ajelah'), ('trainee', 'Trainee'), ('fuel_station', 'Fuel Station'), ('contractor', 'Contractor'), ('freelance', 'Freelancer')], copy=True, required=True, readonly=True, store=True)
    health_card_expiration_date = fields.Date(string='Health Card Expiration Date', copy=True, store=True)
    health_insurance_expiration_date = fields.Date(string='Health Insurance Expiration Date', copy=True, store=True)
    identification_no_expire_date = fields.Date(string='Identification No Expire Date', copy=True, store=True)
    identification_no_issue_date = fields.Date(string='Identification No Issue Date', copy=True, store=True)
    iqama_expire_date = fields.Date(string='Iqama Expire Date', copy=True, store=True)
    iqama_issue_date = fields.Date(string='Iqama Issue Date', copy=True, store=True)
    iqama_no = fields.Char(string='Iqama No', copy=True, store=True)
    job_code = fields.Char(string='Job Position Code', related='job_id.code', readonly=True)
    join_date = fields.Date(string='Join Date', copy=True, store=True)
    passport_expire_date = fields.Date(string='Passport Expire Date', copy=True, store=True)
    passport_issue_date = fields.Date(string='Passport Issue Date', copy=True, store=True)
    payment_method = fields.Selection(string='Payment Method', selection=[('cash_payment', 'Cash Payment'), ('bank_transfer', 'Bank Transfer'), ('cheque', 'Cheque'), ('other', 'Other')], copy=True, store=True)


    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Code must be unique'),
    ]
