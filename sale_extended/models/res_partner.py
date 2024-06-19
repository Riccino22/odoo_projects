from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'
    
    client_type_id = fields.Many2one("sale_extended.client_type")