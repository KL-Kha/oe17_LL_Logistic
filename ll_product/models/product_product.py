# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
    _name = "ll.product.product"
    _description = "LL Product Variant"
    _inherits = {'ll.product.template': 'x_product_tmpl_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, x_default_code, x_name, id'

    x_name = fields.Char('Product Name', index=True)
    x_default_code = fields.Char('Internal Reference', index=True)
    x_code = fields.Char('Reference', compute='_compute_product_code')

    x_product_tmpl_id = fields.Many2one('ll.product.template', 'Product Template',auto_join=True, index=True, ondelete="cascade", required=True)