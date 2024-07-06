from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'  
    discount = fields.Float(string='Discount')

    @api.onchange("product_id")
    def _compute_discount_amount(self):
        # Loop through the product discounts associated with the client's type
        for product in self.order_id.partner_id.client_type_id.product_discounted_ids:
            # Check if the product id matches the selected product in the sale order line
            if product.product_id.id == self.product_id.id:
                # Assign the discount amount to the discount field
                self.discount = product.to_discount
