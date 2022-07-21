from odoo import models, fields


class Session(models.Model):
    _name = "session"
    _description = "Session"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float()
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one("res.partner", domain="[('instructor', '=', True)]")
    course_id = fields.Many2one("course")
    attendee_ids = fields.Many2many("res.partner")
