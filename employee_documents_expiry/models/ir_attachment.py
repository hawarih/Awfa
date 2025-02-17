from odoo import api, fields, models


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel = fields.Many2many(comodel_name='hr.employee.document', string='Attachment', copy=True, relation='doc_attachment_id', column1='attach_id3', column2='doc_id', store=True)
