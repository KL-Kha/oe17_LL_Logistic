# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError


class llSendQuotation(models.TransientModel):
    _name = 'll.sale.order.quotation'
    _description = 'Send Quotation'

    x_name = fields.Char(string="Wizards Name")

    def send_confirm(self):
        pass