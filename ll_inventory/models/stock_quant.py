from odoo import _, api, fields, models, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError

class LLStockQuant(models.Model):
    _name = 'll.stock.quant'
    _description = 'Quants'
    # _rec_name = 'product_id'

    x_name = fields.Char(string="Name")