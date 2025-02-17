from odoo import api, fields, models


class NotificationLog(models.Model):
    _name = 'notification.log'
    _description = 'Notification Log'

    body = fields.Text(string='Body', copy=True, store=True)
    date = fields.Date(string='Date', copy=True, required=True, store=True)
    name = fields.Char(string='Name', copy=True, required=True, store=True)
    user_id = fields.Many2one(comodel_name='res.users', string='User', copy=True, required=True, ondelete='restrict', store=True)
