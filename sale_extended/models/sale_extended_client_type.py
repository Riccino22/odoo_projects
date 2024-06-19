from odoo import models, fields, api

class ProductMod(models.Model):
    _name = "sale_extended.client_type"
    
    name = fields.Char("Name")
    description = fields.Text("Description")
    product_discounted_ids = fields.One2many("sale_extended.product_discounted", inverse_name="client_type_id")
    
    