from odoo import models, fields, api

class ProductDiscounted(models.Model):
    _name = 'sale_extended.product_discounted'
    
    product_id = fields.Many2one("product.template", string="Product")
    client_type_id = fields.Many2one("sale_extended.client_type", string="Client Type")
    amount_to_discount = fields.Float()
    str_discount = fields.Char("Discount", compute="_compute_str_discount")
    
    @api.depends("product_id", "amount_to_discount")
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.amount_to_discount}% - {rec.product_id.name}"
    
    @api.depends("amount_to_discount")
    def _compute_str_discount(self):
        for rec in self:
            rec.str_discount = f"{rec.amount_to_discount}%"
        