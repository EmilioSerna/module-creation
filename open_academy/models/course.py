from odoo import models, fields


class Course(models.Model):
    _name = "open_academy.course"

    title = fields.Char(required=True)
    description = fields.Text()
