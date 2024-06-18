from odoo import models, fields

class MailActivity(models.Model):
    _inherit = "mail.activity"

    # Activity priority
    priority_level = fields.Selection(string="Priority", selection=[
        ('low', 'Low'),
        ('middle', 'Middle'),
        ('high', 'High'),
    ])
    
    # Attachment field if the user wants to upload a file for more description
    attachment = fields.Binary("Attachment")
    
    favorite = fields.Boolean("Favorite")
