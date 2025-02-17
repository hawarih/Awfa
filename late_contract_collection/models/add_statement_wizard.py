from odoo import api, fields, models


class AddStatementWizard(models.TransientModel):
    _name = 'add.statement.wizard'
    _description = 'Add Statement Wizard'

    call_status = fields.Selection(string='Call Status', selection=[('answered', 'Answered'), ('not_answered', 'Not Answered'), ('busy', 'Busy')], copy=True, store=True)
    close_date = fields.Date(string='Close Date', copy=True, store=True)
    contract_id = fields.Many2one(comodel_name='rental.contract', string='Contract', copy=True, store=True)
    details = fields.Text(string='Details', copy=True, store=True)
    extend_date = fields.Date(string='Extend Date', copy=True, store=True)
    statement_status = fields.Selection(string='Statement Status', selection=[('refuse_to_extend_or_deliver', 'Refuse To Extend Or Deliver'), ('pledge_to_deliver', 'Pledge To Deliver'), ('pledge_to_extend', 'Pledge To Extend'), ('objection', 'Objection'), ('other', 'other'), ('customer_is_busy', 'Customer Is Busy')], copy=True, store=True)
    statement_type = fields.Selection(string='Statement Type', selection=[('phone', 'Phone'), ('visit', 'Visit')], copy=True, required=True, store=True)

    def add_statement(self):
        pass