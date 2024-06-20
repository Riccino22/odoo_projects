from odoo import models, fields, api

# Extension of the Sale Order Line model in the sales module
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'  # Inheriting from the existing sale.order.line model
    discount = fields.Float(string='Discount')  # Discount field to store discount amount

    # On change of the product_id field, compute the discount amount
    @api.onchange("product_id")
    def _compute_discount_amount(self):
        # Loop through the product discounts associated with the client's type
        for product in self.order_id.partner_id.client_type_id.product_discounted_ids:
            # Check if the product name matches the selected product in the sale order line
            if product.product_id.name == self.product_id.name:
                # Assign the discount amount to the discount field
                self.discount = product.to_discount
