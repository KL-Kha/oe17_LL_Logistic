# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError

class LLLProductTemplate(models.Model):
    _name = "ll.product.template"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = "LL Product"
    _order = "priority desc, x_name"

    x_name = fields.Char('Name', index='trigram', required=True, translate=True)
    x_sequence = fields.Integer('Sequence', default=1, help='Gives the sequence order when displaying a product list')
    x_description = fields.Html('Description', translate=True)
    x_description_purchase = fields.Text(
        'Purchase Description', translate=True)
    x_description_sale = fields.Text(
        'Sales Description', translate=True,
        help="A description of the Product that you want to communicate to your customers. "
             "This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note")
    x_detailed_type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service')], string='Product Type', default='consu', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')