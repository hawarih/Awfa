from odoo import api, fields, models


class RentalContract(models.Model):
    _inherit = 'rental.contract'

    authorization_country_ids = fields.Many2many(comodel_name='authorization.country', string='Authorization Country', copy=True, relation='authorization_country_rental_contract_rel', column1='rental_contract_id', column2='authorization_country_id', store=True)
    extended_coverage_id = fields.Many2one(comodel_name='extended.coverage', string='Extended Coverage', copy=True, store=True)
    extra_driver_id = fields.Many2one(comodel_name='res.partner', string='Extra Driver', copy=True, store=True)
    main_close_code_id = fields.Many2one(comodel_name='naql.main.close.code', string='Close Reason', copy=True, store=True)
    naql_authorization_type = fields.Selection(string='Authorization Type', selection=[('1', 'Internal'), ('2', 'External')], copy=True, store=True)
    naql_contract_number = fields.Char(string='Naql Contract Number', copy=True, store=True)
    naql_contract_state = fields.Selection(string='Naql Contract State', selection=[('0', 'Not Saved'), ('1', 'Valid'), ('2', 'Closed'), ('3', 'Claim'), 
                                                                                    ('4', 'Canceled'), ('5', 'Pending'), ('6', 'Saved'), 
                                                                                    ('7', 'Pending Under Taqdeer')], copy=True, store=True,
                                                                        default='0')
    naql_id = fields.Integer(string='Naql ID', copy=True, store=True)
    naql_token_number = fields.Char(string='Naql Token Number', copy=True, store=True)
    oil_change_cost = fields.Float(string='Oil Change Cost', copy=True, store=True)
    other1 = fields.Char(string='Other1', copy=True, store=True)
    other2 = fields.Char(string='Other2', copy=True, store=True)
    speedometer = fields.Selection(string='Speedometer Out', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, required=True, store=True)
    sub_close_code_id = fields.Many2one(comodel_name='naql.sub.close.code', string='Sub Reason', copy=True, store=True)
    vehicle_sketch = fields.Text(string='Vehicle Sketch', copy=True, store=True)

    def action_tajeer(self):
        pass
