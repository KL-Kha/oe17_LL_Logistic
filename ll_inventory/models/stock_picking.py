# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import time
from ast import literal_eval
from datetime import date, timedelta
from collections import defaultdict

from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, format_datetime, format_date, groupby
from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class LLPickingType(models.Model):
    _name = "ll.stock.picking.type"
    _description = "LL Picking Type"
    _order = 'x_sequence, id'
    _rec_names_search = ['_rec_names_search']
    _check_company_auto = True

    x_name = fields.Char('Operation Type', required=True, translate=True)
    x_color = fields.Integer('Color')
    x_sequence = fields.Integer('Sequence', help="Used to order the 'All Operations' kanban view")
    x_sequence_id = fields.Many2one('ir.sequence', 'Reference Sequence',check_company=True, copy=False)
    x_sequence_code = fields.Char('Sequence Prefix', required=True)

class LLPicking(models.Model):
    _name = "ll.stock.picking"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Transfer"
    _order = "priority desc, scheduled_date asc, id desc"
    
    x_name = fields.Char(
    'Reference', default='/',
    copy=False, index='trigram', readonly=True)
    x_origin = fields.Char(
        'Source Document', index='trigram',
        help="Reference of the document")
    x_note = fields.Html('Notes')