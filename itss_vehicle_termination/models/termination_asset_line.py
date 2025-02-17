from odoo import api, fields, models


class TerminationAssetLine(models.Model):
    _name = 'termination.asset.line'
    _description = 'Termination Asset Line'

    asset_id = fields.Many2one(comodel_name='account.asset', string='Asset', copy=True,  store=True)
    book_value = fields.Monetary(string='Book Value', copy=True, store=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=True, required=True, readonly=True, ondelete='restrict', store=True)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', related='company_id.currency_id', readonly=True, store=True)
    date = fields.Date(string='Date', copy=True, store=True)
    gain_account_id = fields.Many2one(comodel_name='account.account', string='Gain Account', help="""Account used to write the journal item in case of gain""")
    gain_or_loss = fields.Selection(string='Gain Or Loss', selection=[('gain', 'Gain'), ('loss', 'Loss'), ('no', 'No')], readonly=True)
    invoice_ids = fields.Many2many(comodel_name='account.move', string='Invoice', copy=True, relation='account_move_termination_asset_line_rel', column1='termination_asset_line_id', column2='account_move_id', store=True)
    invoice_line_ids = fields.Many2many(comodel_name='account.move.line', string='Invoice Line', copy=True, relation='account_move_line_termination_asset_line_rel', column1='termination_asset_line_id', column2='account_move_line_id', store=True)
    loss_account_id = fields.Many2one(comodel_name='account.account', string='Loss Account', help="""Account used to write the journal item in case of loss""")
    modify_action = fields.Selection(string='Modify Action', selection=[('dispose', 'Dispose'), ('sell', 'Sell'), ('modify', 'Re-evaluate'), ('pause', 'Pause')], copy=True, store=True)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('confirm', 'Confirm')], store=True, default='draft')
    termination_id = fields.Many2one(comodel_name='vehicle.termination', string='Termination', copy=True,  store=True)

    def sell_dispose(self):
        pass
