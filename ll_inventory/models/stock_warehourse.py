from odoo import _, _lt, api, fields, models
from odoo.exceptions import UserError

class LLWarehouse(models.Model):
    _name = "ll.stock.warehouse"
    _description = "Warehouse"
    _check_company_auto = True

    x_name = fields.Char('Warehouse', required=True, default=_default_name)