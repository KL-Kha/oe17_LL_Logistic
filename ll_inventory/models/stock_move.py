# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, Command, fields, models
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

PROCUREMENT_PRIORITIES = [('0', 'Normal'), ('1', 'Urgent')]

class LLStockMove(models.Model):
    _name = "ll.stock.move"
    _description = "LL Stock Move"
    _order = 'x_sequence, id'

    # def _default_group_id(self):
    #     if self.env.context.get('default_picking_id'):
    #         return self.env['stock.picking'].browse(self.env.context['default_picking_id']).group_id.id
    #     return False

    x_name = fields.Char('Description', required=True)
    x_sequence = fields.Integer('Sequence', default=10)
    x_priority = fields.Selection(PROCUREMENT_PRIORITIES, 'Priority', default='0', store=True)