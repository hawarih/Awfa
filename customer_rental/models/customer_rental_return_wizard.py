from odoo import api, fields, models


class CustomerRentalReturnWizard(models.TransientModel):
    _name = 'customer.rental.return.wizard'
    _description = 'Customer Rental Return Wizard'

    ac = fields.Selection(string='AC In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, required=True, store=True)
    accident_date = fields.Date(string='Accident Date', copy=True, store=True)
    accident_policy = fields.Float(string='Accident Policy', readonly=True)
    announcement_date = fields.Date(string='Announcement Date', copy=True, store=True)
    car_seats = fields.Selection(string='Car Seats In', selection=[('6', 'Clean'), ('7', 'Dirty')], copy=True, required=True, store=True)
    city_id = fields.Many2one(comodel_name='res.country.state', string='City', copy=True, store=True)
    comment = fields.Text(string='Comment', copy=True, store=True)
    damage_state = fields.Selection(string='Damage State', selection=[('nothing', 'Nothing'), ('damage', 'Damage'), ('accident', 'Accident')], copy=True, required=True, store=True)
    drop_off_branch_id = fields.Many2one(comodel_name='stock.location', string='Drop Off Branch', copy=True, store=True)
    fire_extinguisher = fields.Selection(string='Fire Extinguisher In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, required=True, store=True)
    first_aid_kit = fields.Selection(string='First Aid Kit IN', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, required=True, store=True)
    fuel_in = fields.Selection(string='Fuel IN', selection=[('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1')], copy=True, required=True, store=True)
    image1 = fields.Binary(string='Image 1', copy=True, store=True)
    image2 = fields.Binary(string='Image 2', copy=True, store=True)
    image3 = fields.Binary(string='Image 3', copy=True, store=True)
    image4 = fields.Binary(string='Image 4', copy=True, store=True)
    image5 = fields.Binary(string='Image 5', copy=True, store=True)
    image6 = fields.Binary(string='Image 6', copy=True, store=True)
    image7 = fields.Binary(string='Image 7', copy=True, store=True)
    image8 = fields.Binary(string='Image 8', copy=True, store=True)
    insurance_type = fields.Selection(string='Insurance Type', selection=[('full', 'Full Insurance'), ('third', 'Third Party')], copy=True, readonly=True, store=True)
    internal_note = fields.Text(string='Internal Note', copy=True, store=True)
    keys = fields.Selection(string='Keys In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, required=True, store=True)
    km_in = fields.Float(string='Km IN', copy=True, store=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer', copy=True, readonly=True, store=True)
    radio_stereo = fields.Selection(string='Radio Stereo In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, required=True, store=True)
    rental_contract_id = fields.Many2one(comodel_name='rental.contract', string='Rental Contract', copy=True, store=True)
    report_resource = fields.Selection(string='Report Resource', selection=[('nagm', 'Nagm'), ('morror', 'Morror')], copy=True, store=True)
    safety_triangle = fields.Selection(string='Safety Triangle In', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, required=True, store=True)
    screen = fields.Selection(string='Screen In', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak'), ('4', 'Not Working')], copy=True, required=True, store=True)
    spare_tire_tools = fields.Selection(string='Spare Tire Tools IN', selection=[('8', 'Available'), ('9', 'Not Available')], copy=True, required=True, store=True)
    spare_tires = fields.Selection(string='Spare Tires IN', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, required=True, store=True)
    speedometer = fields.Selection(string='Speedometer In', selection=[('4', 'Working'), ('5', 'Not Working')], copy=True, required=True, store=True)
    tires = fields.Selection(string='Tires IN', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Weak')], copy=True, required=True, store=True)
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', copy=True, readonly=True, store=True)
    vehicle_status = fields.Selection(string='Vehicle Status Out', selection=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Simple Scratch'), ('4', 'Deep Scratch'), ('5', 'Very Deep Scratch'), ('6', 'Bend In Structure')], copy=True, required=True, store=True)


    def button_validate(self):
        pass