from odoo import api, fields, models


class NaqlContractLogs(models.Model):
    _name = 'naql.contract.logs'
    _description = 'Naql Contract Logs'

    order_id = fields.Many2one(comodel_name='rental.contract', string='Order', copy=True, ondelete='cascade', store=True)
    response_data = fields.Text(string='Response Data', copy=True, store=True)
    response_status = fields.Char(string='Response Status', copy=True, store=True)
    response_url = fields.Char(string='Response Url', copy=True, store=True)
