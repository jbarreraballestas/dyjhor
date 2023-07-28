# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dyjhor(models.Model):
    _name = 'dyjhor.dyjhor'
    _description = 'dyjhor.dyjhor'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class product(models.Model):
    _name = 'dyjhor.product'
    _description = 'dyjhor.product'

    name = fields.Char()
    price = fields.Float()