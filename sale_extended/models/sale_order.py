from odoo import models, fields, api

# Extension of the Sale Order model in the sales module
class SaleOrder(models.Model):
    _inherit = 'sale.order'  # Inheriting from the existing sale.order model
    
    # Field to store the client type associated with the sale order
    client_type_id = fields.Many2one("sale_extended.client_type", string="Client Type", readonly=True)
    
    # On change of the partner_id field, set the client type
    @api.onchange("partner_id")
    def _set_client_type(self):
        # Assign the client type of the partner to the client_type_id field
        self.client_type_id = self.partner_id.client_type_id
