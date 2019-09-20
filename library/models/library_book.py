# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(String="Book")
    description = fields.Text(string="Description")
