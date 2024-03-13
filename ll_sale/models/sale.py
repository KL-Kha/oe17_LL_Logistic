from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class LLSaleOrder(models.Model):
    _name = "ll.sale.order"
    _description = 'LL Sale Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    x_name = fields.Char(string="Name")
    order_line = fields.One2many(
        comodel_name='sale.order.line',
        inverse_name='order_id',
        string="Order Lines",
        copy=True, auto_join=True)
        
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company.id)

class LLSaleOrderLine(models.Model):
    _name = "ll.sale.order.line"

    _description = 'LL Purchase Order Line'
    _order = 'order_id, sequence, id'

    x_name = fields.Char(string="Name")
    x_sequence = fields.Integer(string="Sequence")
    x_order_id = fields.Many2one('ll.sale.order', string='Order Reference', index=True, required=True, ondelete='cascade')
    company_id = fields.Many2one('res.company', related='x_order_id.company_id', string='Company', store=True, readonly=True)