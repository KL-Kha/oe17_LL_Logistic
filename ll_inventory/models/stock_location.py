# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import calendar

from collections import defaultdict, OrderedDict
from datetime import timedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools.float_utils import float_compare


class LLLocation(models.Model):
    _name = "ll.stock.location"
    _description = "LL Inventory Locations"
    # _parent_name = "location_id"
    # _parent_store = True
    _order = 'x_complete_name, id'
    _rec_name = 'x_complete_name'
    _rec_names_search = ['x_complete_name']
    _check_company_auto = True

    @api.model
    def default_get(self, fields):
        res = super(LLLocation, self).default_get(fields)
        if 'x_barcode' in fields and 'x_barcode' not in res and res.get('x_complete_name'):
            res['x_barcode'] = res['x_complete_name']
        return res

    x_complete_name = fields.Char("Full Location Name", compute='_compute_complete_name', recursive=True, store=True)
    x_company_id = fields.Many2one('res.company', 'Company',default=lambda self: self.env.company, index=True,help='Let this field empty if this location is shared between companies')
    x_barcode = fields.Char('Barcode', copy=False)