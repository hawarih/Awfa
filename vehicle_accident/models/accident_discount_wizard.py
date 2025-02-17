from odoo import api, fields, models


class AccidentDiscountWizard(models.TransientModel):
    _name = 'accident.discount.wizard'
    _description = 'Accident Discount Wizard'

    discount_second = fields.Float(string='Discount Second', copy=True, store=True)
    discount_third = fields.Float(string='Discount Third', copy=True, store=True)
    vehicle_accident_id = fields.Many2one(comodel_name='vehicle.accident', string='Vehicle Accident', copy=True, store=True)

    def action_confirm(self):
        pass
