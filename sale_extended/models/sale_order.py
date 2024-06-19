from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    client_type_id = fields.Many2one("sale_extended.client_type", string="Client Type")
    
    @api.onchange("partner_id")
    def _set_client_type(self):
        self.client_type_id = self.partner_id.client_type_id