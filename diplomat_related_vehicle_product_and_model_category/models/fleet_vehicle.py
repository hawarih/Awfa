from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

import re


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    additional_state = fields.Selection(string='Additional State', selection=[('transfer', 'Transfer'), ('needs_cleaning', 'Needs Cleaning'), ('needs_to_be_transferred_to_branch', 'Needs To Be Transferred To Branch'), ('marked_out_of_service', 'Marked Out Of Service'), ('preventive_maintenance', 'Preventive Maintenance'), ('must_be_returned', 'Must Be Returned'), ('vehicle_license', 'Vehicle License'), ('vehicle_license_check', 'Vehicle License Check'), ('related_to_accident', 'Related To Accident'), ('need_authorization', 'Need Authorization'), ('change_odometer', 'Change Odometer'), ('operational_card', 'Operational Card'), ('missing_plate_number', 'Missing Plate Number'), ('missing_vehicle_key', 'Missing Vehicle Key'), ('stop_booking', 'Stop Booking'), ('vehicle_insurance', 'Vehicle Insurance'), ('waiting_damages_estimation', 'Waiting Damages Estimation'), ('waiting_for_leasing_delivery', 'Waiting For Leasing Delivery'), ('waiting_for_complete_close_contract', 'Waiting For Complete Close Contract'), ('waiting_for_accident_announcement', 'Waiting For Accident Announcement')], copy=True, store=True)
    card_number = fields.Char(string='Card Number', copy=True, store=True)
    color_code = fields.Char(string='Color Code', copy=True, store=True)
    country_id = fields.Many2one(comodel_name='res.country', string='Country', related='company_id.country_id')
    fuel = fields.Selection(string='Fuel', selection=[('0', '0 %'), ('12.5', '12.5 %'), ('25', '25 %'), ('37.5', '37.5 %'), ('50', '50 %'), ('62.5', '62.5 %'), ('75', '75 %'), ('87.5', '87.5 %'), ('100', '100 %')], copy=True, store=True)
    fuel_type = fields.Selection(string='Fuel Type', selection=[('diesel', 'Diesel'), ('petrol_91', 'Petrol 91'), ('petrol_95', 'Petrol 95'), ('gasoline', 'Gasoline'), ('full_hybrid', 'Full Hybrid'), ('plug_in_hybrid_diesel', 'Plug-in Hybrid Diesel'), ('plug_in_hybrid_gasoline', 'Plug-in Hybrid Gasoline'), ('cng', 'CNG'), ('lpg', 'LPG'), ('hydrogen', 'Hydrogen'), ('electric', 'Electric')], copy=True, store=True)
    horse_power = fields.Integer(string='Fuel Tank Size', copy=True, store=True)
    insurance_company = fields.Many2one(comodel_name='res.partner', string='Insurance Company', copy=True, store=True)
    insurance_expiry_date = fields.Date(string='Insurance Expiry Date', copy=True, store=True)
    insurance_number = fields.Char(string='Insurance Number', copy=True, store=True)
    insurance_number_attachment_ids = fields.Many2many(comodel_name='ir.attachment', string='insurance policy', copy=True, relation='fleet_vehicle_ir_attachment_rel', column1='fleet_vehicle_id', column2='ir_attachment_id', store=True)
    license_expiry_date = fields.Date(string='License Expiry Date', copy=True, store=True)
    license_number = fields.Char(string='License Number', copy=True, store=True)
    license_type = fields.Selection(string='License Type', selection=[('special_transportation', 'Special Transportation'), ('private', 'Private'), ('public_transportation', 'Public Transportation')], copy=True, store=True)
    location_id = fields.Many2one(comodel_name='stock.location', string='Location', readonly=True)
    location_id_store = fields.Many2one(comodel_name='stock.location', string='Location Store', copy=True, store=True)
    odometer = fields.Float(string='Last Odometer', help="""Odometer measure of the vehicle at the moment of this log""", store=True)
    power = fields.Integer(string='Engine Size (CC)', help="""Power in kW of the vehicle""", copy=True, store=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', readonly=True, store=True)
    purchase_date = fields.Date(string='Purchase Date', copy=True, store=True)
    serial_number = fields.Char(string='Serial Number', copy=True, store=True)
    source_document = fields.Char(string='Source Document', copy=True, store=True)
    trim_level = fields.Selection(string='Trim Level', selection=[('low', 'low'), ('medium', 'Medium'), ('high', 'High')], copy=True, store=True)
    usage_type = fields.Many2one(comodel_name='usage.type', string='Usage Type', copy=True, store=True)
    vendor_id = fields.Many2one(comodel_name='res.partner', string='Vendor', copy=True, store=True)
    
    
    _sql_constraints = [
        ('fleet_vehicle_unique_card_no', 'unique(card_number)', 'Card Number must be unique'),
        ('fleet_vehicle_unique_license_plate', 'unique(license_plate)', 'Licence Plate must be unique'),
        ('fleet_vehicle_unique_serial_no', 'unique(serial_no)', 'Serial Number must be unique'),
        ('fleet_vehicle_unique_vin_sn', 'unique(vin_sn)', 'Chassis Number must be unique'),
    ]
    
    @api.constrains('license_plate')
    def _check_license_plate_number(self):
        for vehicle in self:
            lic_plate = vehicle.license_plate
            if lic_plate:
                # Check for alphnumeric char and length of the string <= 10 if license plate value is entered.
                if not re.search("^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z0-9]{1,10}$", lic_plate):
                    raise ValidationError(_('License Plate Must be <= 10 character and number.'))
                
    @api.constrains('vin_sn')
    def _check_chassisnumber(self):
        for vehicle in self:
            chase_num = vehicle.vin_sn
            if chase_num:
                # Check for alphnumeric char and length of the string <= 10 if license plate value is entered.
                if not re.search("^.{17}$", chase_num):
                    raise ValidationError(_('Chassis No. must be 17 character or number.'))

    @api.onchange('model_id')
    def _onchange_model_id(self):
        for record in self:
            record.brand_id = record.model_id.brand_id.id
            record.category_id = record.model_id.category_id.id
            record.model_year = record.model_id.model_year
    
    def create_product(self, vehicle, product_name):
        """Create a product related to this vehicle record."""
        return self.env['product.template'].create({
            'name': product_name,
            'rent_ok': True,
            'vehicle_id': vehicle.id,
            'categ_id': vehicle.model_id.categ_id.id if vehicle.model_id.categ_id else False,
            'detailed_type': 'product',
            'invoice_policy': 'delivery',
            'barcode': vehicle.vin_sn if vehicle.vin_sn else False,
            'default_code': vehicle.license_plate if vehicle.license_plate else False
        })
        
    def create_analytic_account(self, vehicle, analytic_account_name):
        """Create a product related to this vehicle record."""
        return self.env['account.analytic.account'].create({
            'name': analytic_account_name,
            'is_vehicle': True,
            'plan_id': self.env['account.analytic.plan'].search([('name', '=', 'Cars'), ('link_with_vehicle', '=', True)], limit=1).id,
            'chassis_num': vehicle.vin_sn if vehicle.vin_sn else False,
            'serial_number': vehicle.serial_number if vehicle.serial_number else False,
        })
    
    def _prepare_product_name(self, vehicle):
        """Prepare the product name based on the vehicle details."""
        license_plate = vehicle.license_plate
        model_name = vehicle.model_id.name or "Unknown Model"
        if not license_plate:
            return f"{model_name}/No Plate"
        return f"{model_name}/{license_plate}"
    
    def _prepare_analytic_account_name(self, vehicle):
        license_plate = vehicle.license_plate
        serial_number = vehicle.serial_number
        if license_plate and serial_number:
            return f"{license_plate} / {serial_number}"
        elif license_plate:
            return f"{license_plate} / No Serial"
        elif serial_number:
            return f"No Plate / {serial_number}"
        return f"No Plate / No Serial"
    
    @api.model_create_multi
    def create(self, vals_list):
        vehicles = super().create(vals_list)
        for vehicle in vehicles:
            analytic_account_name = self._prepare_analytic_account_name(vehicle)
            product_name = self._prepare_product_name(vehicle)
            
            product = self.create_product(vehicle, product_name)
            analytic_account = self.create_analytic_account(vehicle, analytic_account_name)
            
            vehicle.analytic_account_id = analytic_account.id
            vehicle.product_id = product.product_variant_id.id
        return vehicles
    
    def write(self, vals):
        res = super(FleetVehicle, self).write(vals)
        for vehicle in self:
            # Update product information if license_plate changes
            if 'license_plate' in vals:
                vehicle.product_id.name = self._prepare_product_name(vehicle)
                vehicle.product_id.default_code = vals.get('license_plate', vehicle.license_plate)

            # Update product category if model_id changes
            if 'model_id' in vals:
                vehicle.product_id.categ_id = vehicle.model_id.categ_id.id if vehicle.model_id.categ_id else False

            # Update barcode and chassis number
            chase_num = vals.get('vin_sn')
            if chase_num or not chase_num:
                vehicle.product_id.barcode = vehicle.vin_sn
                vehicle.analytic_account_id.chassis_num = vehicle.vin_sn

            # Extract serial_number and license_plate from vals
            serial_number = vals.get('serial_number', vehicle.serial_number)
            license_plate = vals.get('license_plate', vehicle.license_plate)

            # Check if both are False and update analytic_account_id.name accordingly
            if not serial_number and not license_plate:
                vehicle.analytic_account_id.name = "No Plate / No Serial"
                vehicle.analytic_account_id.serial_number = False
            else:
                # Update serial_number if it has changed
                if 'serial_number' in vals:
                    vehicle.analytic_account_id.serial_number = serial_number

                # Update analytic_account_id.name when serial_number or license_plate changes
                if 'serial_number' in vals or 'license_plate' in vals:
                    vehicle.analytic_account_id.name = self._prepare_analytic_account_name(vehicle)

        return res

    def raise_user_error(self, error_causing_fields):
        error = "Data Must Be Unique !!"
        
        for key, field in error_causing_fields.items():
            error += f"\n{key}: {field}, is already exist in vehicle : [{self.name}]"
        raise UserError(error)

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        lic_plate = self.license_plate
        card_num = self.card_number
        serial_num = self.serial_number
        
        if self.search([('card_number', '=', card_num)], limit=1) and card_num:
            raise ValidationError(_('The operation cannot be completed: Card Number must be unique'))
        
        if lic_plate and serial_num:
            self.raise_user_error({'License Plate': lic_plate, 'Serial Number': serial_num})
            
        if serial_num:
            self.raise_user_error({'Serial Number': serial_num})
            
        if lic_plate:
            self.raise_user_error({'License Plate': lic_plate})

        if default is None:
            default = {}
            
        if self.product_id and 'product_id' not in default:
            duplicated_product = self.product_id.copy({'barcode': False})
            default['product_id'] = duplicated_product.id
            
        if self.analytic_account_id and 'analytic_account_id' not in default:
            duplicated_product = self.analytic_account_id.copy({})
            default['analytic_account_id'] = duplicated_product.id

        return super(FleetVehicle, self).copy(default)

    def name_get(self):
        result = []
        for vehicle in self:
            lic_plate = vehicle.license_plate
            if lic_plate:
                name = f"{vehicle.model_id.name} /{lic_plate}"
            else:
                name = f"{vehicle.model_id.name} /No Plate"
            result.append((vehicle.id, name))
        return result
