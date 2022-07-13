from odoo import models, fields


class Course(models.Model):
    _name = "course"
    _description = "Test Course"

    title = fields.Char(required=True)
    description = fields.Text()
