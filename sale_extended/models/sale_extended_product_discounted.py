from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductDiscounted(models.Model):
    _name = 'sale_extended.product_discounted'
    
    product_id = fields.Many2one("product.template", string="Product", required=True)
    client_type_id = fields.Many2one("sale_extended.client_type", string="Client Type")
    amount_to_discount = fields.Float("Disc %")    

    @api.constrains("product_id")
    def _check_product_id(self):
        for rec in self:
            exists = self.search([('product_id', '=', rec.product_id.id), ('client_type_id', '=', rec.client_type_id.id)])
            if len(exists) > 1:
                raise ValidationError(f"The product '{rec.product_id.display_name}' can't be in two records")