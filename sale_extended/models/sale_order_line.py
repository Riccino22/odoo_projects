from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    discount = fields.Float(string='Discount')
    
    @api.onchange("product_id")
    def _compute_discount_amount(self):
        for product in self.order_id.partner_id.client_type_id.product_discounted_ids:
            if product.product_id.name == self.product_id.name:
                self.discount = product.amount_to_discount