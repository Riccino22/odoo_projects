from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Definition of the product discount model in the sales extension module
class ProductDiscounted(models.Model):
    _name = 'sale_extended.product_discounted'
    
    # Fields for the product discount model
    product_id = fields.Many2one("product.template", string="Product", required=True)  # Many-to-one relationship with product template, required field
    client_type_id = fields.Many2one("sale_extended.client_type", string="Client Type")  # Many-to-one relationship with client type
    amount_to_discount = fields.Float("Disc %")  # Discount amount in percentage

    # Constraint to ensure unique product-client type combination
    @api.constrains("product_id")
    def _check_product_id(self):
        for rec in self:
            # Search for existing records with the same product and client type
            exists = self.search([('product_id', '=', rec.product_id.id), ('client_type_id', '=', rec.client_type_id.id)])
            if len(exists) > 1:
                # Raise validation error if a duplicate is found
                raise ValidationError(f"The product '{rec.product_id.display_name}' can't be in two records")
