from odoo import api, fields, models


class ExtendedCoverage(models.Model):
    _name = 'extended.coverage'
    _description = 'Extended Coverage'

    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, translate=True, store=True)
    naql_id = fields.Integer(string='Naql', copy=True, required=True, store=True)
    service_id = fields.Many2one(comodel_name='product.product', string='Service', copy=True, store=True)


    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Name must be unique'),
    ]