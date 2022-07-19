from odoo import models, fields


class Session(models.Model):
    _name = "session"
    _description = "Test Session"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Integer()
    seats = fields.Integer(string="Number of seats")
