# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from re import findall as regex_findall, split as regex_split

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

class LLStockLot(models.Model):
    _name = 'll.stock.lot'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'LL Lot/Serial'
    _check_company_auto = True
    _order = 'x_name, id'

    # x_name = fields.Char('Lot/Serial Number', default=lambda self: self.env['ir.sequence'].next_by_code('stock.lot.serial'),required=True, help="Unique Lot/Serial Number", index='trigram')
    x_name = fields.Char('Lot/Serial Number', default='123456789',required=True, help="Unique Lot/Serial Number", index='trigram')
    x_ref = fields.Char('Internal Reference', help="Internal reference number in case it differs from the manufacturer's lot/serial number")