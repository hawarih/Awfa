from odoo import api, fields, models


class EvaluationParty(models.Model):
    _name = 'evaluation.party'
    _description = 'Evaluation Party'

    name = fields.Char(string='Name', copy=True, store=True)
