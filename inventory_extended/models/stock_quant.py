from odoo import models, api
from odoo.exceptions import ValidationError

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    # Extend the method that computes the inventory_diff field to raise an error message if inventory_quantity is negative
    def _compute_inventory_diff_quantity(self):
        res = super()._compute_inventory_diff_quantity()
        for quant in self:
            if quant.inventory_quantity < 0:
                raise ValidationError("Inventory quantity cannot be negative.")
        return res
