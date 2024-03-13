from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class LLSaleOrder(models.Model):
    _name = "ll.fleet.vehicle"
    _description = 'LL Vehicles'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    x_name = fields.Char(string="Name")
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company.id)