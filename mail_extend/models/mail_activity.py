from odoo import models, fields, api

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
"""    
    created_in_favs = fields.Boolean(computed="_add_to_favs")
    
    @api.depends("favorite")
    def _add_to_favs(self):
        #existing_fav = self.env['mail_extend.fav_activity'].search([('activity_id', '=', self.id)], limit=1)
        for record in self:
            record.priority_level = "low"
            if record.favorite and not record.created_in_favs:
                print(record)
                values = {
                    'activity_id': record.id,
                }
                favs_activs = self.env['mail_extend.fav_activity']
                record.created_in_favs = True
                favs_activs.create(values)
                """