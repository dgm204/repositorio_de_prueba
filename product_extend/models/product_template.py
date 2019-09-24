# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tipology = fields.Selection(
        selection=[
            ['metal', 'Metal'],
            ['pvc', 'PVC'],
            ['cristal', 'Cristal'],
        ]
    )
