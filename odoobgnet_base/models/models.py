# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class odoobgorg_base(models.Model):
#     _name = 'odoobgorg_base.odoobgorg_base'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100