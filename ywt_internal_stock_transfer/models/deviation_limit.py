from odoo import api, fields, models


class DeviationLimit(models.Model):
    _name = 'deviation.limit'
    _description = 'Deviation Limit'

    allowed_time = fields.Float(string='Allowed Time', copy=True, required=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    duplicated = fields.Boolean(string='Duplicated', copy=True, store=True)
    from_location = fields.Many2one(comodel_name='stock.location', string='From', copy=True, required=True, ondelete='restrict', store=True)
    km_limit = fields.Float(string='k.m limit', copy=True, required=True, store=True)
    to_location = fields.Many2one(comodel_name='stock.location', string='To', copy=True, required=True, ondelete='restrict', store=True)

    def duplicate_deviation_limit(self):
        pass