from odoo import api, fields, models


class InspectionWizard(models.TransientModel):
    _name = 'inspection.wizard'
    _description = 'Inspection Wizard'

    ac = fields.Selection(string='Ac', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    car_seats = fields.Selection(string='Car Seats', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, store=True)
    fill_vehicle_info_now = fields.Boolean(string='Fill Vehicle Info Now', copy=True, store=True)
    fire_extinguisher = fields.Selection(string='Fire Extinguisher', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    first_aid_kit = fields.Selection(string='First Aid Kit', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    fuel_type_code = fields.Selection(string='Fuel Type Code', selection=[('1', '91'), ('2', '95'), ('3', 'Diesel'), ('4', 'Electrical')], copy=True, required=True, store=True)
    keys = fields.Selection(string='Keys', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    oil_change_date = fields.Date(string='Oil Change Date', copy=True, store=True)
    oil_change_km_distance = fields.Float(string='Oil Change Km Distance', copy=True, store=True)
    oil_type = fields.Char(string='Oil Type', copy=True, store=True)
    other1 = fields.Char(string='Other1', copy=True, store=True)
    other2 = fields.Char(string='Other2', copy=True, store=True)
    radio_stereo = fields.Selection(string='Radio Stereo', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    safety_triangle = fields.Selection(string='Safety Triangle', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    sale_id = fields.Many2one(comodel_name='sale.order', string='Sale Order', copy=True, store=True)
    screen = fields.Selection(string='Screen', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, store=True)
    spare_tire_tools = fields.Selection(string='Spare Tire Tools', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, store=True)
    spare_tires = fields.Selection(string='Spare Tires', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    speedometer = fields.Selection(string='Speedometer', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, store=True)
    tires = fields.Selection(string='Tires', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, store=True)
    vehicle_sketch = fields.Text(string='Vehicle Sketch', copy=True, store=True)
    vehicle_status = fields.Selection(string='Vehicle Status', selection=[('1', 'خدش بسيط'), ('2', 'خدش عميق'), ('3', 'خدش عميق جدا'), ('4', 'انحناء في الهيكل')], copy=True, store=True)

    def apply(self):
        pass