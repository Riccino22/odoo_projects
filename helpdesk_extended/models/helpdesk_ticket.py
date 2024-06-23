from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    
    suggestion_id = fields.Many2one("helpdesk.category.sug", string="suggestion")