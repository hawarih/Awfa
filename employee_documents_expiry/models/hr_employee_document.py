from odoo import api, fields, models


class HrEmployeeDocument(models.Model):
    _name = 'hr.employee.document'
    _description = 'Hr Employee Document'

    description = fields.Text(string='Description', store=True)
    doc_attachment_id = fields.Many2many(comodel_name='ir.attachment', string='Attachment', help="""You can attach the copy of your document""", relation='doc_attach_rel', column1='doc_id', column2='attach_id3', store=True)
    document_name = fields.Many2one(comodel_name='employee.checklist', string='Document', copy=True, required=True, ondelete='restrict', store=True)
    employee_ref = fields.Many2one(comodel_name='hr.employee', string='Employee Ref', store=True)
    expiry_date = fields.Date(string='Expiry Date', store=True)
    issue_date = fields.Date(string='Issue Date', store=True)
    name = fields.Char(string='Document Number', required=True, store=True)
