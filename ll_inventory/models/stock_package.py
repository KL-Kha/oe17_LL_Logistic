from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class LLStockPackage(models.Model):
    _name = "ll.stock.package"
    _description = 'LL Stock Package'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    x_name = fields.Char(string="Name")