from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Definition of the client type model in the sales extension module
class ProductMod(models.Model):
    _name = "sale_extended.client_type"
    
    # Fields for the client type model
    name = fields.Char("Name", required=True)  # Name of the client type, required field
    description = fields.Text("Description")  # Description of the client type
    product_discounted_ids = fields.One2many("sale_extended.product_discounted", inverse_name="client_type_id")  # One-to-many relationship with product discounts
    discounts = fields.Integer("Discounts", compute="_compute_discounts_quantity")  # Computed field for the number of discounts

    # Compute the display name based on the number of associated product discounts
    @api.depends("name", "product_discounted_ids")
    def _compute_display_name(self):
        for rec in self:
            if len(rec.product_discounted_ids) == 0:
                rec.display_name = f"{rec.name}"  # No discounts
            elif len(rec.product_discounted_ids) == 1:
                rec.display_name = f"{rec.name} - {len(rec.product_discounted_ids)} discount"  # Single discount
            elif len(rec.product_discounted_ids) > 1:
                rec.display_name = f"{rec.name} - {len(rec.product_discounted_ids)} discounts"  # Multiple discounts

    # Compute the quantity of discounts for each client type
    @api.depends("product_discounted_ids")
    def _compute_discounts_quantity(self):
        for rec in self:
            rec.discounts = len(rec.product_discounted_ids)  # Count the number of product discounts

    # Constraint to ensure unique client type names
    @api.constrains("name")
    def _check_client_type_name(self):
        for rec in self:
            exists = self.search([('name', '=', rec.name)])
            if len(exists) > 1:
                raise ValidationError("This contact type name is in use")  # Raise validation error if the name is not unique
