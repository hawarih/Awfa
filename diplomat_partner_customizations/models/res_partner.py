from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birth = fields.Date(string='Date Of Birth', copy=True, store=True)
    commercial_register = fields.Char(string='Commercial Register', copy=True, store=True)
    governmental_no = fields.Char(string='Governmental Number', copy=True, store=True)
    id_expiry = fields.Date(string='Id Expiry Date', copy=True, store=True)
    id_issue = fields.Date(string='Id Issue Date', copy=True, store=True)
    id_type_code = fields.Selection(string='Id Type Code', selection=[('national', 'National'), ('resident', 'Resident'), ('visitor', 'Visitor'), ('citizen_of_the_gcc', 'Citizens of the GCC')], copy=True, store=True)
    id_version_num = fields.Selection(string='Id Version Number', selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], copy=True, store=True)
    license_expiry_date = fields.Date(string='License Expiry Date', copy=True, store=True)
    license_number = fields.Char(string='License Number', copy=True, store=True)
    customized_mobile = fields.Char(string='Mobile', copy=True, store=True)
    mobile = fields.Char(string='Mobile', related='customized_mobile', readonly=True)
    national_identity_number = fields.Char(string='National Identity Number', copy=True, store=True)
    nationality = fields.Many2one(comodel_name='res.country', string='Nationality', copy=True, store=True)
