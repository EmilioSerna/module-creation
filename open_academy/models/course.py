# -*- coding: utf-8 -*-

from odoo import models, fields


class course(models.Model):
    _name = 'course'

    title = fields.Char(required=True)
    description = fields.Text()
