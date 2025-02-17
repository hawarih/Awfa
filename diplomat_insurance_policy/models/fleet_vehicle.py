from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    deductible = fields.Float(string='Deductible', copy=True, store=True)
    end_date = fields.Date(string='End Date', copy=True, readonly=True, store=True)
    has_insurance = fields.Boolean(string='Has Insurance', copy=True, store=True)
    insurance_count = fields.Integer(string='insurance#', readonly=True)
    insurance_id = fields.Many2one(comodel_name='insurance.policy', string='Insurance', readonly=True)
    insurance_type = fields.Selection(string='Insurance Type', selection=[], related='insurance_id.insurance_type', readonly=True)
    start_date = fields.Date(string='Start Date', copy=True, readonly=True, store=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('run', 'Running'), ('stop', 'Stopped')], 
                                                                                            index=True, store=True)
    

    def get_vehicle_insurances(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Insurance Policy',
            'res_model': 'insurance.policy',
            'view_mode': 'tree,form',  # Opens the tree view, allows switching to form view
            'target': 'current',
        }