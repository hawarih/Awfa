from odoo import api, fields, models


class CutWizard(models.TransientModel):
    _name = 'cut.wizard'
    _description = 'Cut Wizard'

    cut_reason = fields.Char(string='Cut Reason', copy=True, store=True, )
    leave_id = fields.Many2one(comodel_name='hr.leave', string='Leave', copy=True, store=True)
    return_date = fields.Date(string='Return Date', copy=True, store=True, )

    def action_confirm(self):
        pass