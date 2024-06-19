from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductMod(models.Model):
    _name = "sale_extended.client_type"
    
    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    product_discounted_ids = fields.One2many("sale_extended.product_discounted", inverse_name="client_type_id")
    discounts = fields.Integer("Discounts", compute="_compute_discounts_quantity")
    @api.depends("name", "product_discounted_ids")
    def _compute_display_name(self):
        for rec in self:
            if len(rec.product_discounted_ids) == 0:            
                rec.display_name = f"{rec.name}"
            elif len(rec.product_discounted_ids) == 1:            
                rec.display_name = f"{rec.name} - {len(rec.product_discounted_ids)} discount"
            elif len(rec.product_discounted_ids) > 1:            
                rec.display_name = f"{rec.name} - {len(rec.product_discounted_ids)} discounts"
    
    @api.depends("product_discounted_ids")
    def _compute_discounts_quantity(self):
        for rec in self:
            rec.discounts = len(rec.product_discounted_ids)
    
    @api.constrains("name")
    def _check_client_type_name(self):
        for rec in self:
            exists = self.search([('name', '=', rec.name)])
            if len(exists) > 1:
                raise ValidationError("This contact type name is in use")