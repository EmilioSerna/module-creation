from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean()
    session_ids = fields.Many2many("session")
