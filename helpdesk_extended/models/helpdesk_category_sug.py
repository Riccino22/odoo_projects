from odoo import models, fields, api

class HelpCategorySug(models.Model):
    _name = "helpdesk.category.sug"
    
    category_name = fields.Char("Category Name")
    description = fields.Text("Category Description")
    user_id = fields.Many2one("res.users", string="User")