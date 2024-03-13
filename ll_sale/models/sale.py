from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class LLSaleOrder(models.Model):
    _name = "ll.sale.order"
    _description = 'LL Sale Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "x_name"
    
    x_name = fields.Char(string="Name")
    x_order_line = fields.One2many(
        comodel_name='ll.sale.order.line',
        inverse_name='x_order_id',
        string="Order Lines",
        copy=True, auto_join=True)
        
    x_company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company.id)

    def button_cancel_payments(self):
        raise ValidationError(_('testing'))

class LLSaleOrderLine(models.Model):
    _name = "ll.sale.order.line"

    _description = 'LL Purchase Order Line'
    _order = 'order_id, sequence, id'

    x_name = fields.Char(string="Name")
    x_sequence = fields.Integer(string="Sequence")
    x_order_id = fields.Many2one('ll.sale.order', string='Order Reference', index=True, required=True, ondelete='cascade')
    x_company_id = fields.Many2one('res.company', related='x_order_id.x_company_id', string='Company', store=True, readonly=True)