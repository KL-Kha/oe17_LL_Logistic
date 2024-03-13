from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class LLAccountMove(models.Model):
    _name = "ll.account.move"
    _description = 'LL Invoicing'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    x_name = fields.Char(string="Name")
    order_line = fields.One2many(
        comodel_name='account.move.line',
        inverse_name='order_id',
        string="Order Lines",
        copy=True, auto_join=True)
        
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company.id)

class LLAccountMoveLine(models.Model):
    _name = "ll.account.move.line"
    _description = 'LL Invoicing Line'
    _order = 'order_id, sequence, id'

    x_name = fields.Char(string="Name")
    x_sequence = fields.Integer(string="Sequence")
    x_order_id = fields.Many2one('ll.account.move', string='Order Reference', index=True, required=True, ondelete='cascade')
    company_id = fields.Many2one('res.company', related='x_order_id.company_id', string='Company', store=True, readonly=True)