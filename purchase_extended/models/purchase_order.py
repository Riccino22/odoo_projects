from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    delete_in = fields.Integer("Delete in (days)")
    
    def _check_date_order(self):
        raise UserError("Deleted")
    
"""    @api.autovacuum
    def _autovacuum_delete_record(self):
        raise UserError("Deleted")"""