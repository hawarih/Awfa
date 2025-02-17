from odoo import api, fields, models


class RentalAdditionalService(models.Model):
    _name = 'rental.additional.service'
    _description = 'Rental Additional Service'

    name = fields.Char(string='Name', copy=True, store=True)
    service_type = fields.Selection(string='Service Status', selection=[('children_seats', 'Children Seats'), ('disabled_service', 'Disabled Service'), ('vehicle_delivery_service', 'Vehicle Delivery Service'), ('navigation_system', 'Navigation System'), ('internet', 'Internet'), ('km_open', 'KM Open')], copy=True, required=True, store=True)


    _sql_constraints = [
        ('service_type_uniq', 'unique(service_type)', 'This service type already created.')
    ]