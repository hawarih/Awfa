from odoo import api, fields, models


class FleetVehicleModel(models.Model):
    _inherit = 'fleet.vehicle.model'

    categ_id = fields.Many2one(comodel_name='product.category', string='Categ', readonly=True, store=True)
    model = fields.Char(string='Model', copy=True, required=True, translate=True, store=True)
    model_year = fields.Integer(string='Model Year', copy=True, required=True, store=True)
    name = fields.Char(string='Model name', required=True, readonly=True, translate=True, store=True)
    
    
    @api.onchange('model', 'brand_id', 'model_year')
    def _create_model_name(self):
        for vehicle_model in self:
            if vehicle_model.model_year and vehicle_model.model and vehicle_model.brand_id:
                vehicle_model.name = vehicle_model.brand_id.name + " / " + vehicle_model.model + " / " + str(vehicle_model.model_year)
            else:
                vehicle_model.name = "Default Model"
                
    def create_product_category(self, categ_name):
        """Create a product category to this record."""
        return self.env['product.category'].create({
            'name': categ_name,
            'is_rental_model': True,
            'property_cost_method': 'fifo',
        })
        
    @api.model_create_multi
    def create(self, values):
        for val in values:
            val.update({'categ_id': self.create_product_category(val.get('name')).id})
        return super().create(values)
    
    def write(self, vals):
        if vals.get('name'):
            self.categ_id.name = vals.get('name')
        
        return super(FleetVehicleModel, self).write(vals)
    
    def name_get(self):
        result = []
        for model in self:
            name = model.name
            result.append((model.id, name))
        return result