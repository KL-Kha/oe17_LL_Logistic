# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import Counter, defaultdict

from odoo import _, api, fields, tools, models, Command
from odoo.exceptions import UserError, ValidationError
from odoo.tools import OrderedSet, groupby
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.addons.base.models.ir_model import MODULE_UNINSTALL_FLAG


class LLStockMoveLine(models.Model):
    _name = "ll.stock.move.line"
    _description = "LL Product Moves (Stock Move Line)"
    # _rec_name = "product_id"
    # _order = "result_package_id desc, id"

    lot_name = fields.Char('Lot/Serial Number Name')